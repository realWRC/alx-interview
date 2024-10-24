#!/usr/bin/python3
"""
A python script solution for alx-interview problems
"""

import sys
import re

total_file_size = 0
status_codes = {}
line_count = 0
valid_status_codes = ['200', '301', '400', '401', '403', '404', '405', '500']

pattern = re.compile(
        r'^(\S+) - \[(.*?)\] "GET /projects/260 HTTP/1\.1" (\d+) (\d+)$'
)


def print_stats():
    print("File size: {}".format(total_file_size))
    for code in sorted(status_codes.keys(), key=int):
        print("{}: {}".format(code, status_codes[code]))


try:
    for line in sys.stdin:
        line = line.strip()
        line_count += 1
        try:
            match = pattern.match(line)
            if match:
                status_code = match.group(3)
                file_size = int(match.group(4))
                total_file_size += file_size
                if status_code in valid_status_codes:
                    status_codes[status_code] = status_codes.get(
                            status_code, 0
                    ) + 1
        except Exception as e:
            pass
        if line_count % 10 == 0:
            print_stats()
except Exception as e:
    pass
