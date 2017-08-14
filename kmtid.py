#!/usr/bin/env python
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-k", "--km", type=int, choices=[2, 3],
                    required=True, help="number of kilometers")
parser.add_argument("-t", "--timer", type=int, default=0, help="timer")
parser.add_argument("-m", "--minutter", type=int, default=0, help="minutter")
parser.add_argument("-s", "--sekunder", type=int, default=0, help="sekunder")
args = parser.parse_args()

import datetime
from datetime import timedelta

total = timedelta(hours=args.timer, minutes=args.minutter, seconds=args.sekunder)

seconds = float(total.total_seconds())/args.km

m, s = divmod(seconds, 60)
h, m = divmod(m, 60)

print "Total: %dt %dm %ds" % (args.timer, args.minutter, args.sekunder)
print "Pr Km: %dt %dm %ds" % (h, m, s)
