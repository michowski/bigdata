#!/usr/bin/env python3

import sys


class AccidentStats:
    def __init__(self):
        self.killed = 0
        self.injured = 0
        self.pedestrians = 0
        self.cyclists = 0
        self.motorists = 0

    def add(self, stats):
        self.killed += stats.killed
        self.injured += stats.injured
        self.pedestrians += stats.pedestrians
        self.cyclists += stats.cyclists
        self.motorists += stats.motorists


aggregated_stats: dict[(str, str), AccidentStats] = {}


for line in sys.stdin:
    values = line.strip().split("\t")

    zip_code = values[0]
    streets = values[1:4]
    affected_people = values[4:10]
    affected_people = map(int, affected_people)
    (
        pedestrians_injured,
        pedestrians_killed,
        cyclists_injured,
        cyclists_killed,
        motorists_injured,
        motorists_killed,
    ) = affected_people

    stats = AccidentStats()

    stats.killed = pedestrians_killed + cyclists_killed + motorists_killed
    stats.injured = pedestrians_injured + cyclists_injured + motorists_injured

    stats.pedestrians = pedestrians_injured + pedestrians_killed
    stats.cyclists = cyclists_injured + cyclists_killed
    stats.motorists = motorists_injured + motorists_killed

    for street in filter(None, streets):
        key = (zip_code, street)

        if not key in aggregated_stats:
            aggregated_stats[key] = stats
        else:
            aggregated_stats[key].add(stats)


for key, stats in aggregated_stats.items():
    (zip_code, street) = key

    print(
        f"{zip_code}\t{street}\t{stats.killed}\t{stats.injured}\t{stats.pedestrians}\t{stats.cyclists}\t{stats.motorists}"
    )
