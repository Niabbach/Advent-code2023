from math import prod
import re


COLORS = ["red", "green", "blue"]

with open("input2.txt") as f:
    games = [re.findall(rf"(\d+) ({'|'.join(COLORS)})", game) for game in f.readlines()]


# ========== PART 1 ==========
MAX_PER_COLOR = dict(zip(COLORS, [12, 13, 14]))


def is_possible(game: list) -> bool:
    for num, color in game:
        if int(num) > MAX_PER_COLOR[color]:
            return False
    return True


print(sum(idx for idx, game in enumerate(games, 1) if is_possible(game)))


# ========== PART 2 ==========
def min_power_set(game: list) -> int:
    counter = dict(zip(COLORS, [0] * 3))
    for num, color in game:
        counter[color] = max(counter[color], int(num))
    return prod(counter.values())


print(sum(min_power_set(game) for game in games))
