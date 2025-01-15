import paramiko
import time

# Intermediate machine details
intermediate_hostname = "10.53.87.119"
intermediate_username = "nutanix"
intermediate_password = "nutanix/4u"

# Target machine details
target_hostname = "10.195.214.110"  # IP address for second SSH login
bash_command = "afs -S"  # Command to open a Bash shell
final_command = "tiering.service_status verbose=true"  # Command to run inside Bash

def nested_ssh_with_interactive_commands():
    try:
        # Step 1: Connect to the intermediate machine
        intermediate_client = paramiko.SSHClient()
        intermediate_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        intermediate_client.connect(intermediate_hostname, username=intermediate_username, password=intermediate_password)
        print(f"Connected to intermediate machine: {intermediate_hostname}")

        # Step 2: Start an interactive shell session on the intermediate machine
        shell = intermediate_client.invoke_shell()
        time.sleep(1)  # Allow the shell to initialize

        # Step 3: SSH to the target machine
        shell.send(f"ssh {target_hostname}\n")
        time.sleep(2)  # Wait for the target machine's SSH prompt
        output = shell.recv(65535).decode()
        print(f"SSH to target machine:\n{output}")

        # Step 4: Open a Bash shell on the target machine
        shell.send(f"{bash_command}\n")
        time.sleep(2)  # Wait for the Bash shell to open
        output = shell.recv(65535).decode()
        print(f"Bash shell opened:\n{output}")

        # Step 5: Run the final command inside Bash
        shell.send(f"{final_command}\n")
        time.sleep(2)  # Wait for the command to execute
        output = shell.recv(65535).decode()
        print(f"Output of the final command:\n{output}")

    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        # Close the connection to the intermediate machine
        intermediate_client.close()
        print("Disconnected from intermediate machine.")

# Run the script
if __name__ == "__main__":
    nested_ssh_with_interactive_commands()
