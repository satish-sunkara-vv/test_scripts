
import os
import subprocess
import time
import sys
import paramiko


#bs=[1,33,67,78,99]
trunc_size=int(input("Please Enter the Truncated size"))
bs=[1,int(trunc_size-(trunc_size/2)),trunc_size-3,int(trunc_size-(trunc_size/2))]

#Connection Details
hostname = "ntnx-10-53-87-119-a-pcvm"
port = 22  # Default SSH port
username = "nutanix"
password = "nutanix/4u"

# Commands to execute
commands = [
    "ssh 10.195.214.110",  # Get system information
    "afs -S",     # Disk usage
    "tiering.service_status verbose=true"     # System uptime
]





















def get_md5sum(file_path):

    command = "md5sum {}".format(file_path)
    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()

    if process.returncode == 0:
        # Decode stdout from bytes to string
        sum1 = stdout.decode('utf-8').strip()
        sum2 = sum1.split()
        return sum1, sum2, None
    else:
        # Decode stderr from bytes to string
        return None, None, stderr.decode('utf-8').strip()

for i in range(101):
    file1="sudo dd if=/home/nutanix/Text_500KB/File-5uK4c.txt  of=/local_test/local_file_${}-512k-64bs.txt bs=64K count=8 conv=notrunc".format(i)
    os.system(file1)
    time.sleep(1)
    file1_create = "/local_test/local_file_{}-512k-64bs.txt".format(i)
    file_path = file1_create
    output, split_output, error = get_md5sum(file_path)
    file1_md5 = str(split_output[0])

    file2 = "sudo dd if=/home/nutanix/Text_500KB/File-5uK4c.txt  of=/mnt/addr_node1_gps1/mount_point_test/local_file_$i-512k-64bs.txt bs=64K count=8 conv=notrunc".format(i)
    os.system(file2)
    time.sleep(1)
    file2_create = "/mnt/addr_node1_gps1/mount_point_test/local_file_{}-512k-64bs.txt".format(i)
    file_path = file2_create
    mp_output, split_output, mp_error = get_md5sum(file_path)
    mp_file_md5 = str(split_output[0])

    if file1_md5 == mp_file_md5:
        print("{}:{}  Md5sum of File creation at Local & MountPoint are MATCHING".format(file1_md5, mp_file_md5))
    else:
        print("The files: {} and {} , md5sum {}:{} check of File creation at Local & MountPoint are NOT MATCHING".format(file1_create, file2_create, file1_md5,mp_file_md5))
        sys.exit()




























for x in range(1001,3001):
    file1="sudo truncate -s -64K  /mnt/addr_node1_gps1/truncdir_n1s1_64k/truncdir_n1s1_64k_${}-512k-64bs.txt".format(x)
    os.system(file1)
    time.sleep(2)
    trunc_file="/mnt/addr_node1_gps1/truncdir_n1s1_64k/truncdir_n1s1_64k_{}-512k-64bs.txt".format(x)
    file_path = trunc_file
    output, split_output, error = get_md5sum(file_path)
    trunc_file_md5 = str(split_output[0])

    file2="sudo dd if=/dev/null of=/mnt/addr_node1_gps1/truncdir_n1s1_64k/truncdir_n1s1_64k_${}-512k-64bs.txt bs=64K count=8 conv=notrunc".format(x)
    os.system(file2)
    time.sleep(1)
    read_trunc_file="/mnt/addr_node1_gps1/truncdir_n1s1_64k/truncdir_n1s1_64k_{}-512k-64bs.txt".format(x)
    file_path = read_trunc_file
    read_output, split_output, read_error = get_md5sum(file_path)
    read_trunc_file_md5 = str(split_output[0])

    if trunc_file_md5 == read_trunc_file_md5:
        print("{}:{}  Md5sum of truncated and after_read are MATCHING".format(trunc_file_md5, read_trunc_file_md5))
    else:
        print("The files: {} and {} , md5sum {}:{} check truncated and after_read are NOT MATCHING".format(trunc_file, read_trunc_file, trunc_file_md5,read_trunc_file_md5))
        sys.exit()

for y in range(1001, 3001):
    file3 = "sudo dd if=/dev/urandom of=/mnt/addr_node1_gps1/truncdir_n1s1_64k/truncdir_n1s1_64k_${}-512k-64bs.txt bs=64K count=1 oflag=append conv=notrunc".format(y)
    os.system(file3)
    time.sleep(1)
    append_trunc_file="/mnt/addr_node1_gps1/truncdir_n1s1_64k/truncdir_n1s1_64k_{}-512k-64bs.txt".format(y)
    file_path = append_trunc_file
    output, split_output, error = get_md5sum(file_path)
    trunc_append_file_md5 = str(split_output[0])

    file4 = "sudo dd if=/dev/null of=/mnt/addr_node1_gps1/truncdir_n1s1_64k/truncdir_n1s1_64k_${}-512k-64bs.txt bs=64K count=8 conv=notrunc".format(y)
    os.system(file4)
    time.sleep(1)
    read_append_trunc_file = "/mnt/addr_node1_gps1/truncdir_n1s1_64k/truncdir_n1s1_64k_{}-512k-64bs.txt".format(y)
    file_path = read_append_trunc_file
    read_output, split_output, read_error = get_md5sum(file_path)
    read_trunc_append_file_md5 = str(split_output[0])

    if trunc_append_file_md5 == read_trunc_append_file_md5:
        print("{}:{}  Md5sum of truncated Append and after_read are MATCHING".format(trunc_append_file_md5, read_trunc_append_file_md5))
    else:
        print("The files: {} and {} , md5sum {}:{} check truncated Append and after_read are NOT MATCHING".format( append_trunc_file,read_append_trunc_file,trunc_append_file_md5, read_trunc_append_file_md5))
        sys.exit()

for i in range(len(bs)):
    for j in range(1001,3001):
        file5="sudo dd if=/dev/urandom of=/mnt/addr_node1_gps1/truncdir_n1s1_64k/truncdir_n1s1_64k_${}-512k-64bs.txt bs={}K count=1 conv=notrunc".format(j,bs[i])
        os.system(file5)
        time.sleep(1)
        overwrite_file="/mnt/addr_node1_gps1/truncdir_n1s1_64k/truncdir_n1s1_64k_{}-512k-64bs.txt".format(j)
        file_path = overwrite_file
        output, split_output, error = get_md5sum(file_path)
        Overwrite_trunc_file_md5 = str(split_output[0])

        file6 = "sudo dd if=/dev/null of=/mnt/addr_node1_gps1/truncdir_n1s1_64k/truncdir_n1s1_64k_${}-512k-64bs.txt bs=64K count=8 conv=notrunc".format(j)
        os.system(file6)
        time.sleep(1)
        read_overwrite_file = "/mnt/addr_node1_gps1/truncdir_n1s1_64k/truncdir_n1s1_64k_{}-512k-64bs.txt".format(j)
        file_path = read_overwrite_file
        read_output, split_output, read_error = get_md5sum(file_path)
        read_overwrite_trunc_file_md5 = str(split_output[0])

        if Overwrite_trunc_file_md5 == read_overwrite_trunc_file_md5:
            print("{}:{}  Md5sum of truncated Append Overwrite and after_read are MATCHING".format(Overwrite_trunc_file_md5,read_overwrite_trunc_file_md5))
        else:
            print("The files: {} and {} , md5sum {}:{} check truncated Append & Overwrite and after_read are NOT MATCHING".format( overwrite_file, read_overwrite_file, Overwrite_trunc_file_md5, read_overwrite_trunc_file_md5))
            sys.exit()



























