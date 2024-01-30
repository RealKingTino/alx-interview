#!/usr/bin/python3
import sys
import signal

def print_statistics(total_size, status_codes):
    print("File size: {:d}".format(total_size))
    for code in sorted(status_codes):
        print("{:d}: {:d}".format(code, status_codes[code]))

def signal_handler(sig, frame):
    print_statistics(total_size, status_codes)
    sys.exit(0)

def parse_line(line, total_size, status_codes):
    try:
        parts = line.split()
        file_size = int(parts[-1])
        status_code = int(parts[-2])

        total_size += file_size

        if status_code in status_codes:
            status_codes[status_code] += 1
        elif status_code in [200, 301, 400, 401, 403, 404, 405, 500]:
            status_codes[status_code] = 1

        return total_size, status_codes

    except Exception:
        return total_size, status_codes

if __name__ == "__main__":
    total_size = 0
    status_codes = {}

    signal.signal(signal.SIGINT, signal_handler)

    try:
        line_count = 0
        for line in sys.stdin:
            line_count += 1
            total_size, status_codes = parse_line(line, total_size, status_codes)

            if line_count == 10:
                print_statistics(total_size, status_codes)
                line_count = 0

    except KeyboardInterrupt:
        print_statistics(total_size, status_codes)
        sys.exit(0)