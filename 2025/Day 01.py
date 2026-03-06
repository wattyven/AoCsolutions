# 2025 aoc day 1
import math

def read_input(filename):
    with open(filename, 'r') as f:
        lines = f.readlines()
        instructions = []
        for line in lines:
            line = line.strip()
            direction = line[0]
            number = int(line[1:])
            instructions.append((direction, number))
    return instructions

def part1(data):
    count = 0
    curnum = 50
    for direction, number in data:
        if direction == 'L':
            curnum -= number
        else:
            curnum += number
        if curnum % 100 == 0: # number of times we land on 0
            count += 1
    return count

def part2(data):
    count = 0
    curnum = 50
    for direction, number in data:
        if direction == 'L': # decreasing the number
            newnum = curnum - number
            lo, hi = newnum, curnum - 1
        else:
            newnum = curnum + number
            lo, hi = curnum + 1, newnum

        if lo <= hi: # safety check
            count += (hi // 100) - math.ceil(lo / 100) + 1 # number of times we pass 0
        curnum = newnum
    return count

if __name__ == "__main__":
    data = read_input('day1.txt')
    print(part1(data))
    print(part2(data))
