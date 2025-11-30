#!/usr/bin/python3
"""
this script reads from stdin and computes metrics.
it parses HTTP request logs to calculate total file size
and status code counts.
"""
import sys


def print_stats(total_size, status_counts):
    """
    prints the accumulated metrics.

    args:
        total_size (int): the sum of all file sizes.
        status_counts (dict): a dictionary of status codes and their counts.
    """
    print("File size: {}".format(total_size))
    for code in sorted(status_counts.keys()):
        if status_counts[code] > 0:
            print("{}: {}".format(code, status_counts[code]))


def main():
    """
    main function to process log lines from stdin.
    """
    total_size = 0
    status_counts = {
        "200": 0, "301": 0, "400": 0, "401": 0,
        "403": 0, "404": 0, "405": 0, "500": 0
    }
    line_count = 0

    try:
        for line in sys.stdin:
            # parse the line
            parts = line.split()

            # We need at least 2 elements (status and size) to proceed
            if len(parts) >= 2:
                try:
                    # extract Metrics
                    # File size is the last element
                    size = int(parts[-1])

                    # status code is the second to last element
                    code = parts[-2]

                    # aggregate
                    total_size += size
                    if code in status_counts:
                        status_counts[code] += 1

                except (ValueError, IndexError):
                    # skip lines with invalid integers or bad formats
                    pass

            # periodic Reporting (Every 10 lines)
            line_count += 1
            if line_count % 10 == 0:
                print_stats(total_size, status_counts)

        # end of stream: Print final stats
        print_stats(total_size, status_counts)

    except KeyboardInterrupt:
        # handle CTRL+C gracefully
        print_stats(total_size, status_counts)
        raise


if __name__ == "__main__":
    main()
