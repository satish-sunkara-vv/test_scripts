
import paramiko
import time
import sys

# Intermediate machine details
intermediate_hostname = "10.53.87.119"
intermediate_username = "nutanix"
intermediate_password = "nutanix/4u"

# Target machine details
target_hostname = "10.195.214.110"
bash_command = "afs -S"

# Client machine details
client_hostname = "10.53.87.122"
port = 22
client_username = "nutanix"
client_password = "nutanix/4u"

def filter_output(raw_output):
    """Filter unnecessary login banners or messages."""
    unwanted_phrases = [
        "Last login:",
        "Nutanix Prism Central VM",
        "Nutanix File-Server VM",
        "Alteration of the PCVM",
        "Alteration of the FSVM",
        "Unsupported alterations",
        "Please consider using the 'admin'",
        "FIPS mode initialized",
        "of User VMs or other data residing on the cluster.",
        "sources (using yum, rpm, or similar).",
        "Support Portal Documentation",
        "unsupported and may result in loss",
        "Configuration changes",
        "Installation of third-party software",
        "Installation or upgrade of software packages",
        "** SSH to PCVM via 'nutanix' user will be restricted"
    ]
    filtered_lines = [
        # line for line in raw_output.split("\n") if not any(phrase in line for phrase in unwanted_phrases)
        line for line in raw_output.split("\n")
        if line.strip() and not any(phrase in line for phrase in unwanted_phrases)
    ]
    return "\n".join(filtered_lines)

def nested_ssh_with_interactive_commands(final_command):
    try:
        intermediate_client = paramiko.SSHClient()
        intermediate_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        intermediate_client.connect(intermediate_hostname, username=intermediate_username, password=intermediate_password)
        print(f"Connected to intermediate machine: {intermediate_hostname}")

        shell = intermediate_client.invoke_shell()
        time.sleep(1)

        # SSH to the target machine
        shell.send(f"ssh {target_hostname}\n")
        time.sleep(2)
        output = filter_output(shell.recv(65535).decode())
        print(f"Filtered output after SSH to target machine:\n{output}")

        # Open a Bash shell on the target machine
        shell.send(f"{bash_command}\n")
        time.sleep(2)
        output = filter_output(shell.recv(65535).decode())
        print(f"Filtered output after opening Bash shell:\n{output}")

        # Execute the final command
        shell.send(f"{final_command}\n")
        time.sleep(2)
        output = filter_output(shell.recv(65535).decode())
        print(f"Filtered output of the final command:\n{output}")

    except Exception as e:
        print(f"An error occurred during nested SSH: {e}")
    finally:
        intermediate_client.close()
        print("Disconnected from intermediate machine.")

def execute_remote_command(ssh_client, command):
    stdin, stdout, stderr = ssh_client.exec_command(command)
    stdout_output = stdout.read().decode().strip()
    stderr_output = stderr.read().decode().strip()
    return stdout_output, stderr_output

if __name__ == "__main__":
    try:
        ssh_client = paramiko.SSHClient()
        ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh_client.connect(client_hostname, port, client_username, client_password)
        print(f"Connected to {client_hostname}")

        for i in range(46, 60):
            #File Creation at Cloud FSVM(Mount point) and Local to the Client
            file1 = f"sudo dd if=/home/nutanix/Text_500KB/File-5uK4c.txt of=/mnt/addr_node1_gps1/mount_point_test/test_md5_{i}.txt bs=64K count=8 conv=notrunc"
            execute_remote_command(ssh_client, file1)
            time.sleep(1)

            file1_test = f"/mnt/addr_node1_gps1/mount_point_test/test_md5_{i}.txt"
            file1_md5_command = f"sudo md5sum {file1_test}"
            output, error = execute_remote_command(ssh_client, file1_md5_command)
            file1_chksum = output.split()
            print(f"File:test_md5_{i}.txt at MountPoint and Check sum is {file1_chksum[0]}:")

            file2 = f"sudo dd if=/home/nutanix/Text_500KB/File-5uK4c.txt of=/local_test/test_md5_{i}.txt bs=64K count=8 conv=notrunc"
            execute_remote_command(ssh_client, file2)
            time.sleep(1)

            file2_test = f"/local_test/test_md5_{i}.txt"
            file2_md5_command = f"sudo md5sum {file2_test}"
            file2_output, file2_error = execute_remote_command(ssh_client, file2_md5_command)
            file2_chksum = file2_output.split()
            print(f"File:test_md5_{i}.txt at Local   and  Check sum is {file2_chksum[0]}:")

            if file1_chksum[0] == file2_chksum[0]:
                print(f"{file1_chksum[0]}:{file2_chksum[0]} MD5 checksums local/cloud are MATCH")
            else:
                print(f"MD5 checksums local/cloud are MISMATCH: {file1_chksum[0]} vs {file2_chksum[0]}")
                sys.exit()

            # File Tier with command comapare md5sum with and Local on the Client
            final_command = f"tiering.tier addr_node1_gps1 file_paths=mount_point_test/test_md5_{i}.txt"
            nested_ssh_with_interactive_commands(final_command)
            time.sleep(1)

            file3_test = f"/mnt/addr_node1_gps1/mount_point_test/test_md5_{i}.txt"
            file3_md5_command = f"sudo md5sum {file3_test}"
            output, error = execute_remote_command(ssh_client, file1_md5_command)
            file3_chksum = output.split()
            print(f"File:test_md5_{i}.txt at After tier & Checksum is  {file3_chksum[0]}:")
            print(f"File:test_md5_{i}.txt at Local   and  Check sum is {file2_chksum[0]}:")

            if file3_chksum[0] == file2_chksum[0]:
                print(f"{file3_chksum[0]}:{file2_chksum[0]} MD5 checksums After tier MATCH")
            else:
                print(f"MD5 checksums After tier MISMATCH: {file3_chksum[0]} vs {file2_chksum[0]}")
                sys.exit()

            #Files Truncate at the cloud FSVM and Local machine

            file4 = f"sudo truncate -s -64K /mnt/addr_node1_gps1/mount_point_test/test_md5_{i}.txt"
            execute_remote_command(ssh_client, file4)
            time.sleep(1)

            file4_test = f"/mnt/addr_node1_gps1/mount_point_test/test_md5_{i}.txt"
            file4_md5_command = f"sudo md5sum {file4_test}"
            output, error = execute_remote_command(ssh_client, file4_md5_command)
            file4_chksum = output.split()
            print(f"File:test_md5_{i}.txt at MountPoint and Check sum is {file4_chksum[0]}:")

            file5 = f"sudo truncate -s -64K /local_test/test_md5_{i}.txt "
            execute_remote_command(ssh_client, file5)
            time.sleep(1)

            file5_test = f"/local_test/test_md5_{i}.txt"
            file5_md5_command = f"sudo md5sum {file5_test}"
            file5_output, file5_error = execute_remote_command(ssh_client, file5_md5_command)
            file5_chksum = file5_output.split()
            print(f"File:test_md5_{i}.txt at Local   and  Check sum is {file5_chksum[0]}:")

            if file4_chksum[0] == file5_chksum[0]:
                print(f"{file4_chksum[0]}:{file5_chksum[0]} MD5 checksums local/cloud After Truncate are MATCH")
            else:
                print(f"MD5 checksums local/cloud After Truncate are MISMATCH: {file4_chksum[0]} vs {file5_chksum[0]}")
                sys.exit()

            # Files Appending the same data after Truncate at the cloud FSVM and Local machine

            file6 = f"sudo dd if=/home/nutanix/Text_500KB/File-5uK4c.txt of=/mnt/addr_node1_gps1/mount_point_test/test_md5_{i}.txt bs=64K count=1 oflag=append conv=notrunc"
            execute_remote_command(ssh_client, file6)
            time.sleep(1)

            file6_test = f"/mnt/addr_node1_gps1/mount_point_test/test_md5_{i}.txt"
            file6_md5_command = f"sudo md5sum {file6_test}"
            output, error = execute_remote_command(ssh_client, file6_md5_command)
            file6_chksum = output.split()
            print(f"File:test_md5_{i}.txt at MountPoint and Check sum is {file6_chksum[0]}:")

            file7 = f"sudo dd if=/home/nutanix/Text_500KB/File-5uK4c.txt of=/local_test/test_md5_{i}.txt bs=64K count=1 oflag=append conv=notrunc"
            execute_remote_command(ssh_client, file7)
            time.sleep(1)

            file7_test = f"/local_test/test_md5_{i}.txt"
            file7_md5_command = f"sudo md5sum {file7_test}"
            file7_output, file7_error = execute_remote_command(ssh_client, file7_md5_command)
            file7_chksum = file7_output.split()
            print(f"File:test_md5_{i}.txt at Local   and  Check sum is {file7_chksum[0]}:")

            if file6_chksum[0] == file7_chksum[0]:
                print(f"{file4_chksum[0]}:{file5_chksum[0]} MD5 checksums local/cloud files append After Truncate are MATCH")
            else:
                print(f"MD5 checksums local/cloud files append After Truncate are MISMATCH: {file6_chksum[0]} vs {file7_chksum[0]}")
                sys.exit()

            #Overwriting the Files after Truncate/append Completed
            bs=[32,78]
            for x in range(2):
                if x == 0:
                    z=bs[0]
                else:
                    z=bs[1]
                file8 = f"sudo dd if=/home/nutanix/Text_500KB/File-5uK4c.txt of=/mnt/addr_node1_gps1/mount_point_test/test_md5_{i}.txt bs={z}K count=1 conv=notrunc"
                execute_remote_command(ssh_client, file8)
                time.sleep(1)

                file8_test = f"/mnt/addr_node1_gps1/mount_point_test/test_md5_{i}.txt"
                file8_md5_command = f"sudo md5sum {file8_test}"
                output, error = execute_remote_command(ssh_client, file8_md5_command)
                file8_chksum = output.split()
                print(f"File:test_md5_{i}.txt at MountPoint and Check sum is {file8_chksum[0]}:")

                file9 = f"sudo dd if=/home/nutanix/Text_500KB/File-5uK4c.txt of=/local_test/test_md5_{i}.txt bs={z}K count=1 conv=notrunc"
                execute_remote_command(ssh_client, file9)
                time.sleep(1)

                file9_test = f"/local_test/test_md5_{i}.txt"
                file9_md5_command = f"sudo md5sum {file9_test}"
                file9_output, file9_error = execute_remote_command(ssh_client, file9_md5_command)
                file9_chksum = file9_output.split()
                print(f"File:test_md5_{i}.txt at Local   and  Check sum is {file9_chksum[0]}:")

                if file8_chksum[0] == file9_chksum[0]:
                    print(f"{file4_chksum[0]}:{file5_chksum[0]} MD5 checksums local/cloud Over-write with {z}K After append & Truncate are MATCH")
                else:
                    print(f"MD5 checksums local/cloud Over-write with {z}K After append &After Truncate are MISMATCH: {file8_chksum[0]} vs {file9_chksum[0]}")
                    sys.exit()

    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        ssh_client.close()
        print("Disconnected from remote machine.")
