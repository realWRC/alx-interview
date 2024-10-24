#!/usr/bin/python3
# """
# A python script solution for alx-interview problems
# """
#
# import sys
# import re
#
# total_file_size = 0
# status_codes = {}
# line_count = 0
# valid_status_codes = ['200', '301', '400', '401', '403', '404', '405', '500']
#
# pattern = re.compile(
#         r'^(\S+) - \[(.*?)\] "GET /projects/260 HTTP/1\.1" (\d+) (\d+)$'
# )
#
#
# def print_stats():
#     print("File size: {}".format(total_file_size))
#     for code in sorted(status_codes.keys(), key=int):
#         print("{}: {}".format(code, status_codes[code]))
#
#
# try:
#     for line in sys.stdin:
#         line = line.strip()
#         try:
#             match = pattern.match(line)
#             if match:
#                 status_code = match.group(3)
#                 file_size = int(match.group(4))
#                 total_file_size += file_size
#                 if status_code in valid_status_codes:
#                     status_codes[status_code] = status_codes.get(
#                             status_code, 0
#                     ) + 1
#                 line_count += 1
#             if line_count % 10 == 0:
#                 print_stats()
#         except Exception as e:
#             pass
# except KeyboardInterrupt:
#     print_stats()
#     raise
"""
Write a script that reads stdin line by line and computes metrics:
"""


import sys

# store the count of all status codes in a dictionary
status_codes_dict = {'200': 0, '301': 0, '400': 0, '401': 0, '403': 0,
                     '404': 0, '405': 0, '500': 0}

total_size = 0
count = 0  # keep count of the number lines counted

try:
    for line in sys.stdin:
        line_list = line.split(" ")

        if len(line_list) > 4:
            status_code = line_list[-2]
            file_size = int(line_list[-1])

            # check if the status code receive exists in the dictionary and
            # increment its count
            if status_code in status_codes_dict.keys():
                status_codes_dict[status_code] += 1

            # update total size
            total_size += file_size

            # update count of lines
            count += 1

        if count == 10:
            count = 0  # reset count
            print('File size: {}'.format(total_size))

            # print out status code counts
            for key, value in sorted(status_codes_dict.items()):
                if value != 0:
                    print('{}: {}'.format(key, value))

except Exception as err:
    pass

finally:
    print('File size: {}'.format(total_size))
    for key, value in sorted(status_codes_dict.items()):
        if value != 0:
            print('{}: {}'.format(key, value))
