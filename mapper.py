#!/usr/bin/env python3

import sys
import re

OUTPUT_SIZE = 10
OUTPUT_FORMAT = "{}\t" * (OUTPUT_SIZE - 1) + "{}"


def parse_int(x: str):
    return int(x) if len(x.strip()) else 0


for line in sys.stdin:
    values = line.split(",")

    crash_date = values[0]
    date_year_match = re.search(r"\d{4}", crash_date)

    # Filtr: Tylko od roku > 2012
    if not date_year_match:
        continue
    if int(date_year_match.group()) <= 2012:
        continue

    # Filtr: Tylko z poprawnym kodem pocztowym
    zip_code = values[2]
    if not re.match(r"\d{5}", zip_code):
        continue

    on_street_name = values[6]
    cross_street_name = values[7]
    off_street_name = values[8]
    number_of_pedestrians_injured = parse_int(values[11])
    number_of_pedestrians_killed = parse_int(values[12])
    number_of_cyclist_injured = parse_int(values[13])
    number_of_cyclist_killed = parse_int(values[14])
    number_of_motorist_injured = parse_int(values[15])
    number_of_motorist_killed = parse_int(values[16])

    print(
        OUTPUT_FORMAT.format(
            zip_code,
            on_street_name,
            cross_street_name,
            off_street_name,
            number_of_pedestrians_injured,
            number_of_pedestrians_killed,
            number_of_cyclist_injured,
            number_of_cyclist_killed,
            number_of_motorist_injured,
            number_of_motorist_killed,
        )
    )
