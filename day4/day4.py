filename = 'input4.txt'

cards = []

with open(filename) as f:
    for line in f.readlines():
        card_numbers, winning_numbers = line.strip().replace('  ', ' ').split(': ')[1].split(' | ')
        cards.append(
            (
                set([c.strip() for c in card_numbers.split(' ')]),
                set([w.strip() for w in winning_numbers.split(' ')])
            )
        )

def part1(cards):
    answer = 0
    for card_numbers, winning_numbers in cards:
        intersection = card_numbers.intersection(winning_numbers)
        points = 1 * 2 ** (len(intersection) - 1) if intersection else 0
        answer += points

    return answer

def score_card(i, cards, score=0):
    score += 1
    card_numbers, winning_numbers = cards[i]
    intersection = len(card_numbers.intersection(winning_numbers))
    next_card_i = i + 1
    for j in range(next_card_i, next_card_i + intersection):
        score = score_card(j, cards, score)
    return score

def part2(cards):
    score = 0
    for i in range(0, len(cards)):
        score += score_card(i, cards)
    return score

print(part1(cards))

print(part2(cards))