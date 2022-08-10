import argparse
import numpy as np
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
        return amt * 63360
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
        return amt/63360
    elif unit == "cm":
        return amt * 2.54
    elif unit == "m":
        return amt * 2.54 / 100
    elif unit == "km":
        return amt * 2.54 / 100000
def crossProduct(array):
    return np.cross(array[:3], array[-3:])

def main():
    parser = argparse.ArgumentParser(prog = "length unit converter")
    parser.add_argument("input_amount", type = float, help = "input amount")
    parser.add_argument("input_unit", choices = ["in", "ft", "yd", "mi", "cm", "m", "km"], help = "unit of the input amount")
    parser.add_argument("output_unit", choices = ["in", "ft", "yd", "mi", "cm", "m", "km"], help = "unit you want to convert to")
    parser.add_argument("-c", "--cross_product", type =  int, nargs = 6, help = "takes the cross product of two vectors, first 3 numbers represent one vector, last 3 numbers represent other vector")
    parser.add_argument("-v", "--verbosity", help = "increase output verbosity", action = "count", default = 0)
    args = parser.parse_args()

    # do the conversion
    output_amount = inchToUnit(args.output_unit, unitToInch(args.input_unit, args.input_amount))
    
    # print out more text if the verbosity is 1 or more
    if args.verbosity >= 1:
        print(str(args.input_amount) + args.input_unit + " is " + str(output_amount) + args.output_unit)
    else:
        print(str(output_amount) + args.output_unit)
    
    # print out the cross product if the optional argument was called
    if(args.cross_product):
        print(crossProduct(args.cross_product))

# run the main function if this file is directly run
if __name__ == '__main__':
    main()
    