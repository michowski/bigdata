#!/usr/bin/env python3

import sys

last_key = None
current_count = 0


def print_current_count():
    print(f"{last_key}\t{current_count}")


for line in sys.stdin:
    key, count = line.strip().split("\t")

    if last_key != key:
        if last_key != None:
            print_current_count()

        last_key = key
        current_count = 0

    current_count += int(count)

if last_key != None:
    print_current_count()
