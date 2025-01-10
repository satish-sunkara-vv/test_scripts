# import os
# import time
#
# for b in range(101)
#     def complete_read_with_dd(start=3000, end=6001, sleep_interval=1):
#         for a in range(start, end):
#             file_command = (
#                 "sudo dd if=/dev/null of=/mnt/addr_node1_gps1/truncdir_n1s1_64k/truncdir_n1s1_64k_${}-512k-64bs.txt bs=64K count=8 conv=notrunc".format(a)
#             )
#             os.system(file_command)
#             time.sleep(sleep_interval)
#     bs=[100,175,219,260,310]
#     for x in range(3000,6001):
#         file="sudo truncate -s -300K  /mnt/addr_node1_gps1/truncdir_n1s1_64k/truncdir_n1s1_64k_${}-512k-64bs.txt".format(x)
#         os.system(file)
#         time.sleep(1)
#     complete_read_with_dd()
#     for y in range(3000,6001):
#         file="sudo dd if=/dev/urandom of=/mnt/addr_node1_gps1/truncdir_n1s1_64k/truncdir_n1s1_64k_${}-512k-64bs.txt bs=300K count=5 oflag=append conv=notrunc".format(y)
#         os.system(file)
#         time.sleep(1)
#     complete_read_with_dd()
#     for i in range(len(bs)):
#         for j in range(3000,6001):
#             if i<len(bs):
#                 file1="sudo dd if=/dev/urandom of=/mnt/addr_node1_gps1/truncdir_n1s1_64k/truncdir_n1s1_64k_${}-512k-64bs.txt bs={}K count=1 conv=notrunc".format(j,bs[i])
#                 os.system(file1)
#                 time.sleep(1)
#         complete_read_with_dd()
#
#
#
#
# import os
# import time
#
# def complete_read_with_dd(start=6000, end=9001, sleep_interval=1):
#     for a in range(start, end):
#         file_command ="sudo dd if=/dev/null of=/mnt/addr_node1_gps1/truncdir_n1s1_64k/truncdir_n1s1_64k_${}-512k-64bs.txt bs=64K count=8 conv=notrunc".format(a)
#         os.system(file_command)
#         time.sleep(sleep_interval)
#
# bs=[100,219,350,410,460]
# for x in range(6000,9001):
#     file="sudo truncate -s -455K  /mnt/addr_node1_gps1/truncdir_n1s1_64k/truncdir_n1s1_64k_${}-512k-64bs.txt".format(x)
#     os.system(file)
#     time.sleep(1)
# complete_read_with_dd()
# for y in range(6000,9001):
#     file="sudo dd if=/dev/urandom of=/mnt/addr_node1_gps1/truncdir_n1s1_64k/truncdir_n1s1_64k_${}-512k-64bs.txt bs=455K count=1 oflag=append conv=notrunc".format(y)
#     os.system(file)
#     time.sleep(1)
# complete_read_with_dd()
# for i in range(len(bs)):
#     for j in range(6000,9001):
#         if i<len(bs):
#             file1="sudo dd if=/dev/urandom of=/mnt/addr_node1_gps1/truncdir_n1s1_64k/truncdir_n1s1_64k_${}-512k-64bs.txt bs={}K count=1 conv=notrunc".format(j,bs[i])
#             os.system(file1)
#             time.sleep(1)
#     complete_read_with_dd()



#Truncate and check md5sum


# import os
# import time
#
#
# for x in range(1,3001):
#     file1="sudo truncate -s -64K  /mnt/addr_node1_gps1/truncdir_n1s1_64k/truncdir_n1s1_64k_${}-512k-64bs.txt".format(x)
#     os.system(file1)
#     time.sleep(3)
#     m1="md5sum /mnt/addr_node1_gps1/truncdir_n1s1_64k/truncdir_n1s1_64k_${}-512k-64bs.txt".format(x)
#     sum1=os.system(m1)
#     time.sleep(1)
#     file2="sudo dd if=/dev/null of=/mnt/addr_node1_gps1/truncdir_n1s1_64k/truncdir_n1s1_64k_${}-512k-64bs.txt bs=64K count=8 conv=notrunc".format(x)
#     os.system(file2)
#     time.sleep(1)
#     m2 = "md5sum /mnt/addr_node1_gps1/truncdir_n1s1_64k/truncdir_n1s1_64k_${}-512k-64bs.txt".format(x)
#     sum2 = os.system(m2)
#     time.sleep(1)
#     if sum1==sum2:
#         print("{}:{}  are matching".format(sum1,sum2))
#     else:
#         print("The file: truncdir_n1s1_64k_${}-512k-64bs.txt , md5sum {}:{}check is not matching".format(x,sum1,sum2))
#         break
#
# for y in range(1,101):
#     file1="sudo dd if=/dev/urandom of=/mnt/addr_node1_gps1/truncdir_n1s1_64k/truncdir_n1s1_64k_${}-512k-64bs.txt bs=455K count=1 oflag=append conv=notrunc".format(y)
#     os.system(file1)
#     time.sleep(1)
#     m1 = "md5sum /mnt/addr_node1_gps1/truncdir_n1s1_64k/truncdir_n1s1_64k_${}-512k-64bs.txt".format(y)
#     sum1 = os.system(m1)
#     time.sleep(1)
#     file2 = "sudo dd if=/dev/null of=/mnt/addr_node1_gps1/truncdir_n1s1_64k/truncdir_n1s1_64k_${}-512k-64bs.txt bs=64K count=8 conv=notrunc".format(y)
#     os.system(file2)
#     time.sleep(1)
#     m2 = "md5sum /mnt/addr_node1_gps1/truncdir_n1s1_64k/truncdir_n1s1_64k_${}-512k-64bs.txt".format(y)
#     sum2 = os.system(m2)
#     time.sleep(1)
#     if sum1==sum2:
#         print("{}:{}  are matching".format(sum1,sum2))
#     else:
#         print("The file: truncdir_n1s1_64k_${}-512k-64bs.txt , md5sum {}:{}check is not matching".format(x,sum1,sum2))
#         break
#
# for i in range(len(bs)):
#     for j in range(1,101):
#         if i<len(bs):
#             file1="sudo dd if=/dev/urandom of=/mnt/addr_node1_gps1/truncdir_n1s1_64k/truncdir_n1s1_64k_${}-512k-64bs.txt bs={}K count=1 conv=notrunc".format(j,bs[i])
#             os.system(file1)
#             time.sleep(1)
#             m1 = "md5sum /mnt/addr_node1_gps1/truncdir_n1s1_64k/truncdir_n1s1_64k_${}-512k-64bs.txt".format(j)
#             sum1 = os.system(m1)
#             time.sleep(1)
#             file2 = "sudo dd if=/dev/null of=/mnt/addr_node1_gps1/truncdir_n1s1_64k/truncdir_n1s1_64k_${}-512k-64bs.txt bs=64K count=8 conv=notrunc".format(j)
#             os.system(file2)
#             time.sleep(1)
#             m2 = "md5sum /mnt/addr_node1_gps1/truncdir_n1s1_64k/truncdir_n1s1_64k_${}-512k-64bs.txt".format(j)
#             sum2 = os.system(m2)
#             time.sleep(1)
#             if sum1 == sum2:
#                 print("{}:{}  are matching".format(sum1, sum2))
#             else:
#                 print("The file: truncdir_n1s1_64k_${}-512k-64bs.txt , md5sum {}:{}check is not matching".format(j, sum1,sum2))
#                 break


###################################################################################################################################################


import os
import subprocess
import time
import sys

bs=[1,33,67,78,99]

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

for x in range(1,3001):
    file1="sudo truncate -s -64K  /mnt/addr_node1_gps1/truncdir_n1s1_64k/truncdir_n1s1_64k_${}-512k-64bs.txt".format(x)
    os.system(file1)
    time.sleep(2)
    trunc_file="/mnt/addr_node1_gps1/truncdir_n1s1_64k/truncdir_n1s1_64k_${}-512k-64bs.txt".format(x)
    file_path = trunc_file
    output, split_output, error = get_md5sum(file_path)
    trunc_file_md5 = str(split_output[0])

    file2="sudo dd if=/dev/null of=/mnt/addr_node1_gps1/truncdir_n1s1_64k/truncdir_n1s1_64k_${}-512k-64bs.txt bs=64K count=8 conv=notrunc".format(x)
    os.system(file2)
    time.sleep(1)
    read_trunc_file="/mnt/addr_node1_gps1/truncdir_n1s1_64k/truncdir_n1s1_64k_${}-512k-64bs.txt".format(x)
    file_path = read_trunc_file
    read_output, split_output, read_error = get_md5sum(file_path)
    read_trunc_file_md5 = str(split_output[0])

    if trunc_file_md5 == read_trunc_file_md5:
        print("{}:{}  Md5sum of truncated and after_read are MATCHING".format(trunc_file_md5, read_trunc_file_md5))
    else:
        print("The files: {} and {} , md5sum {}:{} check truncated and after_read are NOT MATCHING".format(trunc_file, read_trunc_file, trunc_file_md5,read_trunc_file_md5))
        sys.exit()

for y in range(1, 3001):
    file3 = "sudo dd if=/dev/urandom of=/mnt/addr_node1_gps1/truncdir_n1s1_64k/truncdir_n1s1_64k_${}-512k-64bs.txt bs=64K count=1 oflag=append conv=notrunc".format(y)
    os.system(file3)
    time.sleep(1)
    append_trunc_file="/mnt/addr_node1_gps1/truncdir_n1s1_64k/truncdir_n1s1_64k_${}-512k-64bs.txt".format(y)
    file_path = append_trunc_file
    output, split_output, error = get_md5sum(file_path)
    trunc_append_file_md5 = str(split_output[0])

    file4 = "sudo dd if=/dev/null of=/mnt/addr_node1_gps1/truncdir_n1s1_64k/truncdir_n1s1_64k_${}-512k-64bs.txt bs=64K count=8 conv=notrunc".format(y)
    os.system(file4)
    time.sleep(1)
    read_append_trunc_file = "/mnt/addr_node1_gps1/truncdir_n1s1_64k/truncdir_n1s1_64k_${}-512k-64bs.txt".format(y)
    file_path = read_append_trunc_file
    read_output, split_output, read_error = get_md5sum(file_path)
    read_trunc_append_file_md5 = str(split_output[0])

    if trunc_append_file_md5 == read_trunc_append_file_md5:
        print("{}:{}  Md5sum of truncated Append and after_read are MATCHING".format(trunc_append_file_md5, read_trunc_append_file_md5))
    else:
        print("The files: {} and {} , md5sum {}:{} check truncated Append and after_read are NOT MATCHING".format( append_trunc_file,read_append_trunc_file,trunc_append_file_md5, read_trunc_append_file_md5))
        sys.exit()

for i in range(len(bs)):
    for j in range(1,3001):
        file5="sudo dd if=/dev/urandom of=/mnt/addr_node1_gps1/truncdir_n1s1_64k/truncdir_n1s1_64k_${}-512k-64bs.txt bs={}K count=1 conv=notrunc".format(j,bs[i])
        os.system(file5)
        time.sleep(1)
        overwrite_file="/mnt/addr_node1_gps1/truncdir_n1s1_64k/truncdir_n1s1_64k_${}-512k-64bs.txt".format(j)
        file_path = overwrite_file
        output, split_output, error = get_md5sum(file_path)
        Overwrite_trunc_file_md5 = str(split_output[0])

        file6 = "sudo dd if=/dev/null of=/mnt/addr_node1_gps1/truncdir_n1s1_64k/truncdir_n1s1_64k_${}-512k-64bs.txt bs=64K count=8 conv=notrunc".format(j)
        os.system(file6)
        time.sleep(1)
        read_overwrite_file = "/mnt/addr_node1_gps1/truncdir_n1s1_64k/truncdir_n1s1_64k_${}-512k-64bs.txt".format(j)
        file_path = read_overwrite_file
        read_output, split_output, read_error = get_md5sum(file_path)
        read_overwrite_trunc_file_md5 = str(split_output[0])

        if Overwrite_trunc_file_md5 == read_overwrite_trunc_file_md5:
            print("{}:{}  Md5sum of truncated Append Overwrite and after_read are MATCHING".format(Overwrite_trunc_file_md5,read_overwrite_trunc_file_md5))
        else:
            print("The files: {} and {} , md5sum {}:{} check truncated Append & Overwrite and after_read are NOT MATCHING".format( overwrite_file, read_overwrite_file, Overwrite_trunc_file_md5, read_overwrite_trunc_file_md5))
            sys.exit()



























