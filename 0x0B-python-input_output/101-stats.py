#!/usr/bin/python3
"""
This module deals with file I/O operations.

"""
import sys


def print_metrics(metrics):
    """
    Read stdin and compute metrics.

    """
    total_size = metrics['total_size']
    status_codes = metrics['status_codes']

    print("File size: {}".format(total_size))

    for code in sorted(status_codes):
        print("{}: {}".format(code, status_codes[code]))


def main():
    metrics = {
            'total_size': 0,
            'status_codes': {
                200: 0,
                301: 0,
                400: 0,
                401: 0,
                403: 0,
                404: 0,
                405: 0,
                500: 0
            }
    }
    count = 0

    try:
        for line in sys.stdin:
            count += 1
            item = line.split()
            if len(item) >= 9:
                status_code = int(item[8])
                file_size = int(item[10])
                metrics['total_size'] += file_size
                if status_code in metrics['status_codes']:
                    metrics['status_codes'][status_code] += 1

            if count == 10:
                print_metrics(metrics)
                count = 0

    except KeyboardInterrupt:
        pass

    print_metrics(metrics)

if __name__ == "__main__":
    main()
