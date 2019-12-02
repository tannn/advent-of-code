import os
import math
THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
input_file = os.path.join(THIS_FOLDER, 'day1input.txt')

def part1(inputfile):
    summ = 0
    with open(inputfile) as f:
        for item in f:
            item = int(item)
            item = math.floor(item/3)
            item -= 2
            summ += item
    print(summ)

#part1(input_file)

def calculate(item):
    summation = 0
    while item > 0:
        item = math.floor(item/3)
        item -= 2
        if item > 0:
            summation += item

    return summation

def part2(inputfile):
    summ = 0
    with open(inputfile) as f:
        for item in f:
            item = int(item)
            summ += calculate(item)
    print(summ)

part2(input_file)