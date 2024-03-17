#!/usr/bin/env python3

import sys

last_key: tuple[str, str] = None
current_count = 0


def print_current_count():
    (month, zone) = last_key
    print(f"{month}\t{zone}\t{current_count}")


for line in sys.stdin:
    values = line.strip().split("\t")
    (month, zone, count) = values

    key = (month, zone)

    if last_key != key:
        if last_key != None:
            print_current_count()

        last_key = key
        current_count = 0

    current_count += int(count)


print_current_count()
