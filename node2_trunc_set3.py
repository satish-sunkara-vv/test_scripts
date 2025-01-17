#
# import os
# import subprocess
# import time
# import sys
#
# #bs=[1,33,67,78,99]
# trunc_size=int(input("Please Enter the Truncated size :"))
# bs=[1,int(trunc_size-(trunc_size/2)),trunc_size-3,int(trunc_size+(trunc_size/2))]
#
# def get_md5sum(file_path):
#
#     command = "md5sum {}".format(file_path)
#     process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     stdout, stderr = process.communicate()
#
#     if process.returncode == 0:
#         # Decode stdout from bytes to string
#         sum1 = stdout.decode('utf-8').strip()
#         sum2 = sum1.split()
#         return sum1, sum2, None
#     else:
#         # Decode stderr from bytes to string
#         return None, None, stderr.decode('utf-8').strip()
#
# for x in range(6001,10001):
#     file1="sudo truncate -s -{}K  /mnt/addr_node2_gps2/truncdir_n2s2_12M/truncdir_n2s2_64k_${}-12M-1mbs.txt".format(trunc_size,x)
#     os.system(file1)
#     time.sleep(1)
#     trunc_file="/mnt/addr_node2_gps2/truncdir_n2s2_12M/truncdir_n2s2_64k_{}-12M-1mbs.txt".format(x)
#     file_path = trunc_file
#     output, split_output, error = get_md5sum(file_path)
#     trunc_file_md5 = str(split_output[0])
#
#     file2="sudo dd if=/dev/null of=/mnt/addr_node2_gps2/truncdir_n2s2_12M/truncdir_n2s2_64k_${}-12M-1mbs.txt conv=notrunc".format(x)
#     os.system(file2)
#     time.sleep(1)
#     read_trunc_file="/mnt/addr_node2_gps2/truncdir_n2s2_12M/truncdir_n2s2_64k_{}-12M-1mbs.txt".format(x)
#     file_path = read_trunc_file
#     read_output, split_output, read_error = get_md5sum(file_path)
#     read_trunc_file_md5 = str(split_output[0])
#
#     if trunc_file_md5 == read_trunc_file_md5:
#         print("{}:{}  Md5sum of truncated and after_read are MATCHING".format(trunc_file_md5, read_trunc_file_md5))
#     else:
#         print("The files: {} and {} , md5sum {}:{} check truncated and after_read are NOT MATCHING".format(trunc_file, read_trunc_file, trunc_file_md5,read_trunc_file_md5))
#         sys.exit()
#
# for y in range(6001,10001):
#     file3 = "sudo dd if=/dev/urandom of=/mnt/addr_node2_gps2/truncdir_n2s2_12M/truncdir_n2s2_64k_${}-12M-1mbs.txt bs={}K count=1 oflag=append conv=notrunc".format(y,trunc_size)
#     os.system(file3)
#     time.sleep(1)
#     append_trunc_file="/mnt/addr_node2_gps2/truncdir_n2s2_12M/truncdir_n2s2_64k_{}-12M-1mbs.txt".format(y)
#     file_path = append_trunc_file
#     output, split_output, error = get_md5sum(file_path)
#     trunc_append_file_md5 = str(split_output[0])
#
#     file4 = "sudo dd if=/dev/null of=/mnt/addr_node2_gps2/truncdir_n2s2_12M/truncdir_n2s2_64k_${}-12M-1mbs.txt conv=notrunc".format(y)
#     os.system(file4)
#     time.sleep(1)
#     read_append_trunc_file = "/mnt/addr_node2_gps2/truncdir_n2s2_12M/truncdir_n2s2_64k_{}-12M-1mbs.txt".format(y)
#     file_path = read_append_trunc_file
#     read_output, split_output, read_error = get_md5sum(file_path)
#     read_trunc_append_file_md5 = str(split_output[0])
#
#     if trunc_append_file_md5 == read_trunc_append_file_md5:
#         print("{}:{}  Md5sum of truncated Append and after_read are MATCHING".format(trunc_append_file_md5, read_trunc_append_file_md5))
#     else:
#         print("The files: {} and {} , md5sum {}:{} check truncated Append and after_read are NOT MATCHING".format( append_trunc_file,read_append_trunc_file,trunc_append_file_md5, read_trunc_append_file_md5))
#         sys.exit()
#
# for i in range(len(bs)):
#     for j in range(6001,10001):
#         file5="sudo dd if=/dev/urandom of=/mnt/addr_node2_gps2/truncdir_n2s2_12M/truncdir_n2s2_64k_${}-12M-1mbs.txt bs={}K count=1 conv=notrunc".format(j,bs[i])
#         os.system(file5)
#         time.sleep(1)
#         overwrite_file="/mnt/addr_node2_gps2/truncdir_n2s2_12M/truncdir_n2s2_64k_{}-12M-1mbs.txt".format(j)
#         file_path = overwrite_file
#         output, split_output, error = get_md5sum(file_path)
#         Overwrite_trunc_file_md5 = str(split_output[0])
#
#         file6 = "sudo dd if=/dev/null of=/mnt/addr_node2_gps2/truncdir_n2s2_12M/truncdir_n2s2_64k_${}-12M-1mbs.txt conv=notrunc".format(j)
#         os.system(file6)
#         time.sleep(1)
#         read_overwrite_file = "/mnt/addr_node2_gps2/truncdir_n2s2_12M/truncdir_n2s2_64k_{}-12M-1mbs.txt".format(j)
#         file_path = read_overwrite_file
#         read_output, split_output, read_error = get_md5sum(file_path)
#         read_overwrite_trunc_file_md5 = str(split_output[0])
#
#         if Overwrite_trunc_file_md5 == read_overwrite_trunc_file_md5:
#             print("{}:{}  Md5sum of truncated Append Overwrite and after_read are MATCHING".format(Overwrite_trunc_file_md5,read_overwrite_trunc_file_md5))
#         else:
#             print("The files: {} and {} , md5sum {}:{} check truncated Append & Overwrite and after_read are NOT MATCHING".format( overwrite_file, read_overwrite_file, Overwrite_trunc_file_md5, read_overwrite_trunc_file_md5))
#             sys.exit()
#
#
#
#
# ###################################################################################################################################

import os
import time


bs=[1,300,670,780,1250]
for a in range(100):
    for x in range(2):
        for y in range(1,5001):
            file="sudo dd if=/dev/zero of=/mnt/addr_node2_gps2/holedir_n2s2_12M/holedir_n2s2_64k_${}-12M-1mbs.txt bs=1M seek={} count=1 conv=notrunc".format(y,x+9)
            os.system(file)
            time.sleep(1)
        for k in range(1,5001):
            file="sudo dd if=/dev/null of=/mnt/addr_node2_gps2/holedir_n2s2_12M/holedir_n2s2_64k_${}-12M-1mbs.txt bs=1M count=12 conv=notrunc".format(k)
            os.system(file)
            time.sleep(1)
        for i in range(len(bs)):
            for j in range(1,5001):
                if i<len(bs):
                    file1="sudo dd if=/dev/urandom of=/mnt/addr_node2_gps2/holedir_n2s2_12M/holedir_n2s2_64k_${}-12M-1mbs.txt seek={} bs={}K count=1 conv=notrunc".format(j,x+9,bs[i])
                    os.system(file1)
                    time.sleep(1)
            for z in range(1,5001):
                file2="sudo dd if=/dev/null of=/mnt/addr_node2_gps2/holedir_n2s2_12M/holedir_n2s2_64k_${}-12M-1mbs.txt bs=1M count=12 conv=notrunc".format(z)
                os.system(file2)
                time.sleep(1)
