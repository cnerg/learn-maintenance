import argparse
from itertools import count
from random import choices

def unitToInch(unit, amt):
    if unit == "in":
        return amt
    elif unit == "ft":
        return amt * 12
    elif unit == "yd":
        return amt * 36
    elif unit == "mi":
        return amt * 15840
    elif unit == "cm":
        return amt/2.54
    elif unit == "m":
        return amt/2.54 * 100
    elif unit == "km":
        return amt/2.54 * 100000

def inchToUnit(unit, amt):
    if unit == "in":
        return amt
    elif unit == "ft":
        return amt/12
    elif unit == "yd":
        return amt/36
    elif unit == "mi":
        return amt/15840
    elif unit == "cm":
        return amt * 2.54
    elif unit == "m":
        return amt * 2.54 / 100
    elif unit == "km":
        return amt * 2.54 / 100000

# TODO add argparser here
def main():
    parser = argparse.ArgumentParser(prog = "number guesser")
    parser.add_argument("input_amount", type = float, help = "input amount")
    parser.add_argument("input_unit", choices = ["in", "ft", "yd", "mi", "cm", "m", "km"], help = "unit of the input amount")
    parser.add_argument("output_unit", choices = ["in", "ft", "yd", "mi", "cm", "m", "km"], help = "unit you want to convert to")
    parser.add_argument("-v", "--verbosity", help = "increase output verbosity", action = "count", default = 0)
    args = parser.parse_args()

    output_amount = inchToUnit(args.output_unit, unitToInch(args.input_unit, args.input_amount))
    if args.verbosity >= 1:
        print(str(args.input_amount) + args.input_unit + " is " + str(output_amount) + args.output_unit)
    else:
        print(str(output_amount) + args.output_unit)

if __name__ == '__main__':
    main()
    