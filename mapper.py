#!/usr/bin/env python3

import sys
import re


PAYMENT_TYPE_MONEY = "2"

for line in sys.stdin:
    values = line.split(",")

    payment_type = values[9]
    if payment_type != PAYMENT_TYPE_MONEY:
        continue

    pickup_date = values[1]
    month_match = re.search(r"^\d{4}-(\d{2})", pickup_date)
    month = int(month_match.group(1))

    count = values[3]
    zone = values[7]

    print(f"{month},{zone}\t{count}")
