import itertools


def get_universe(file: str) -> list:
    return open(file).read().splitlines()


def get_vertical_expansions(universe: list):
    amount = 0
    for y in range(len(universe)):
        for x in range(len(universe[0])):
            if universe[y][x] == '#':
                break
        else:
            amount += 1

        yield amount


def get_horizontal_espansions(universe: list):
    amount = 0
    for x in range(len(universe[0])):
        for y in range(len(universe)):
            if universe[y][x] == '#':
                break
        else:
            amount += 1

        yield amount


def get_galaxies(universe: list):
    for y in range(len(universe)):
        for x in range(len(universe[0])):
            if universe[y][x] == '#':
                yield x, y


def adjusted_coordinate(expansion_factor: 1, coordinate: tuple, expansions_horizontal: tuple, expansions_vertical: tuple):
    x, y = coordinate
    return x + expansions_horizontal[x] * expansion_factor, y + expansions_vertical[y] * expansion_factor


def manhattan_distance(coordinate_1: tuple, coordinate_2: tuple) -> int:
    x1, y1 = coordinate_1
    x2, y2 = coordinate_2

    return abs(x1 - x2) + abs(y1 - y2)


def main(file: str, expansion_factor: int) -> int:
    universe = get_universe(file)
    expansions_horizontal = tuple(expansion for expansion in get_horizontal_espansions(universe))
    expansions_vertical = tuple(expansion for expansion in get_vertical_expansions(universe))
    coordinates = (coordinate for coordinate in get_galaxies(universe))

    coordinates_adjusted = (
        adjusted_coordinate(
            expansion_factor,
            coordinate,
            expansions_horizontal,
            expansions_vertical
        )
        for coordinate in coordinates
    )
    distances = (
        manhattan_distance(coordinate_1, coordinate_2)
        for coordinate_1, coordinate_2 in itertools.combinations(coordinates_adjusted, 2)
    )
    return sum(distances)


if __name__ == '__main__':
    print('par1_1', main('input11.txt', 1))
    print('part_2', main('input11.txt', 1_000_000 - 1))
