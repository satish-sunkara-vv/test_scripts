

import os
import subprocess
import time
import sys

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

seek=0
bs=[1,33,67,78,99]
for x in range(9):
    for y in range(1001,9001):
        file1="sudo dd if=/dev/zero of=/mnt/addr_node1_gps1/holedir_n1s1_64k/holedir_n1s1_64k_${}-512k-64bs.txt bs=64K seek={} count=1 conv=notrunc".format(y,x+1)
        os.system(file1)
        time.sleep(1)
        hole_file = "/mnt/addr_node1_gps1/holedir_n1s1_64k/holedir_n1s1_64k_{}-512k-64bs.txt".format(y)
        file_path = hole_file
        output, split_output, error = get_md5sum(file_path)
        hole_file_md5 = str(split_output[0])

        file2 = "sudo dd if=/dev/null of=/mnt/addr_node1_gps1/holedir_n1s1_64k/holedir_n1s1_64k_${}-512k-64bs.txt bs=64K count=8 conv=notrunc".format(y)
        os.system(file2)
        time.sleep(1)
        read_file = "/mnt/addr_node1_gps1/holedir_n1s1_64k/holedir_n1s1_64k_{}-512k-64bs.txt".format(y)
        file_path = read_file
        read_output, split_output, read_error = get_md5sum(file_path)
        read_file_md5 = str(split_output[0])

        if hole_file_md5 == read_file_md5:
            print("{}:{}  Md5sum of Hole_after_read are matching".format(hole_file_md5, read_file_md5))
        else:
            print("The files: {} and {} , md5sum {}:{}check is not matching".format(hole_file,read_file, hole_file_md5,read_file_md5))
            sys.exit()
    print("----------------------------------------------------punched hole at :{} block--------------------------------------------".format(x))

    for i in range(len(bs)):
        for j in range(1001,9001):
            file3="sudo dd if=/dev/urandom of=/mnt/addr_node1_gps1/holedir_n1s1_64k/holedir_n1s1_64k_${}-512k-64bs.txt seek={} bs={}K count=1 conv=notrunc".format(j,x+1,bs[i])
            os.system(file3)
            time.sleep(1)
            aos_hole_file = "/mnt/addr_node1_gps1/holedir_n1s1_64k/holedir_n1s1_64k_{}-512k-64bs.txt".format(j)
            file_path = aos_hole_file
            output, split_output, error = get_md5sum(file_path)
            aos_hole_file_md5 = str(split_output[0])

            file4 = "sudo dd if=/dev/null of=/mnt/addr_node1_gps1/holedir_n1s1_64k/holedir_n1s1_64k_${}-512k-64bs.txt bs=64K count=8 conv=notrunc".format(j)
            os.system(file4)
            time.sleep(1)
            aos_read_hole_file = "/mnt/addr_node1_gps1/holedir_n1s1_64k/holedir_n1s1_64k_{}-512k-64bs.txt".format(j)
            file_path = aos_read_hole_file
            aos_read_output, split_output, aos_read_error = get_md5sum(file_path)
            aos_read_hole_file_md5 = str(split_output[0])

            if aos_hole_file_md5 == aos_read_hole_file_md5:
                print("{}:{}  are matching".format(aos_hole_file_md5, aos_read_hole_file_md5))
            else:
                print("The files: {} and {} , md5sum {}:{}check is not matching".format(aos_hole_file,aos_read_hole_file,aos_hole_file_md5,aos_read_hole_file_md5))
                sys.exit()
        print("---------------------------------------------------------------------------------------Over write on punched hole at block Size:{}KB------------------------------------".format(bs[i]))




