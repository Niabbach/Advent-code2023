#!/bin/python3

from copy import deepcopy
import sys
from typing import List

FILE = sys.argv[1] if len(sys.argv) > 1 else "input19.txt"


def read_lines_to_list() -> List[str]:
    lines: List[str] = []

    with open(FILE, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            lines.append(line)

    return lines


def parse(lines):
    instructions = {}
    ratings = []
    is_ratings = False
    for line in lines:
        if len(line) == 0:
            is_ratings = True
            continue

        if not is_ratings:
            l = line.split("{")
            name = l[0]
            parts = [part.split(":") for part in l[1][:-1].split(",")]
            parts = [
                [(part[0][0], part[0][1], int(part[0][2:])), part[1]]
                if len(part) == 2
                else part
                for part in parts
            ]
            instructions[name] = parts
        else:
            l = [a.split("=") for a in line[1:-1].split(",")]
            l = dict((k, int(v)) for [k, v] in l)
            ratings.append(l)

    return (instructions, ratings)


def part_one():
    lines = read_lines_to_list()
    answer = 0

    (instructions, ratings) = parse(lines)

    for rating in ratings:
        curr = "in"
        while curr not in ["A", "R"]:
            rules = instructions[curr]
            for r in rules:
                if len(r) == 1:
                    curr = r[0]
                    break
                else:
                    (var, condition, value) = r[0]
                    result = r[1]

                    if condition == ">":
                        if rating[var] > value:
                            curr = result
                            break
                    else:
                        if rating[var] < value:
                            curr = result
                            break

        if curr == "A":
            answer += sum(rating.values())

    print(f"Part 1: {answer}")


def range_size(range):
    result = 1
    for val in range.values():
        result *= 1 + val[1] - val[0]
    return result


def solve(instructions, range, curr: str):
    parts = instructions[curr]
    val = 0

    for part in parts:
        if len(part) == 1:
            if part[0] == "A":
                val += range_size(range)
            elif part[0] != "R":
                val += solve(instructions, range, part[0])
        else:
            (var, cond, amount) = part[0]
            destination = part[1]

            range_var = range[var]

            if cond == ">":
                if range_var[1] > amount:
                    range_copy = deepcopy(range)
                    range_copy[var] = (max(range_var[0], amount + 1), range_var[1])

                    if destination == "A":
                        val += range_size(range_copy)
                    elif destination != "R":
                        val += solve(instructions, range_copy, destination)

                # continue search as if it failed
                range[var] = (range_var[0], amount)
            else:
                if range_var[0] < amount:
                    range_copy = deepcopy(range)
                    range_copy[var] = (range_var[0], min(range_var[1], amount - 1))

                    if destination == "A":
                        val += range_size(range_copy)
                    elif destination != "R":
                        val += solve(instructions, range_copy, destination)

                # continue search as if it failed
                range[var] = (amount, range_var[1])

    return val


def part_two():
    lines = read_lines_to_list()

    (instructions, _) = parse(lines)
    range = {}
    for val in "xmas":
        range[val] = (1, 4000)
    answer = solve(instructions, range, "in")

    print(f"Part 2: {answer}")


part_one()
part_two()
