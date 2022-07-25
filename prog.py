import argparse
from itertools import count
from random import choices
import random

parser = argparse.ArgumentParser()
parser.add_argument("input", type = int, help = "guess for a random 1 digit number", choices = range(10))
parser.add_argument("-v", "--verbosity", help = "increase output verbosity", action = "count", default = 0)
args = parser.parse_args()
num = random.randrange(0,10)

if args.input == num:
    outcome = "right"
else:
    outcome = "wrong"
if args.verbosity >= 2:
    print("Your guess was " + outcome + ". The correct number was " + str(num))
elif args.verbosity >= 1:
    print("Your guess was " + outcome + ".")
else:
    print(outcome)
    