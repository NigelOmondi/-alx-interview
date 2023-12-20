#!/usr/bin/env python3
"""
Log Parsing
"""
import sys
import re
import signal


def signal_handler(sig, frame):
    print_statistics()
    sys.exit(0)


def print_statistics():
    print(f"File size: {total_size}")
    for code in sorted(status_codes.keys()):
        print(f"{code}: {status_codes[code]}")


# Register the signal handler for CTRL+C
signal.signal(signal.SIGINT, signal_handler)

# Regular expression to match the log line format
log_line_regex = r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}) - \[(.*?)\] "GET /projects/260 HTTP/1.1" (\d+) (\d+)'

# Initialize variables
total_size = 0
status_codes = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
line_count = 0

try:
    for line in sys.stdin:
        # Match the line with the regular expression
        match = re.match(log_line_regex, line)
        if match:
            status_code = int(match.group(3))
            file_size = int(match.group(4))

            # Update total file size and status code count
            total_size += file_size
            if status_code in status_codes:
                status_codes[status_code] += 1

        line_count += 1
        if line_count % 10 == 0:
            print_statistics()
except KeyboardInterrupt:
    # Handle CTRL+C interruption
    print_statistics()
    sys.exit(0)
