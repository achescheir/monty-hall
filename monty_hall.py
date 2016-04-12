import random
from unittest import mock


def get_prizes(number_of_prizes, doors):
    doors_left = doors[:]
    prizes = []
    for i in range(number_of_prizes):
        prize = random.choice(doors_left)
        prizes.append(prize)
        doors_left.remove(prize)
    return prizes


def get_opened_doors(doors, chosen, prizes, number_to_open):
    doors_left = [x for x in doors if (x != chosen and x not in prizes)]
    opened = []
    for i in range(number_to_open):
        to_open = random.choice(doors_left)
        opened.append(to_open)
        doors_left.remove(to_open)
    return opened


def swap(doors, chosen, opened):
    doors_left = [x for x in doors if (x not in opened and x != chosen)]
    return random.choice(doors_left)


def play_round(will_swap=True, num_of_doors=3, num_of_prizes=1, num_to_open=1):
    doors = list(range(num_of_doors))
    prizes = get_prizes(num_of_prizes, doors)
    chosen = random.choice(doors)
    opened = get_opened_doors(doors, chosen, prizes, num_to_open)
    if will_swap:
        chosen = swap(doors, chosen, opened)
    return chosen in prizes


def main():
    will_swap = True
    num_of_doors = 3
    num_of_prizes = 1
    num_to_open = 1
    wins = 0
    losses = 0
    for _ in range(100000):
        win = play_round(will_swap, num_of_doors, num_of_prizes, num_to_open)
        if win:
            wins += 1
        else:
            losses += 1
    winrate = 100 * wins / (wins + losses)
    print("Swapper:")
    print('{}, wins and {} losses. {}% winrate.'.format(wins, losses, winrate))
    print("")
    will_swap = False
    wins = 0
    losses = 0
    for _ in range(100000):
        win = play_round(will_swap, num_of_doors, num_of_prizes, num_to_open)
        if win:
            wins += 1
        else:
            losses += 1
    winrate = 100 * wins / (wins + losses)
    print("Non-Swapper:")
    print('{}, wins and {} losses. {}% winrate.'.format(wins, losses, winrate))
    print('')

if __name__ == '__main__':
    main()
