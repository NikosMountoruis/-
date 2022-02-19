import random
import itertools


def check_game_over(squaredic):
    end = []
    for i in range(1, 3):
        if set(squaredic[i]).intersection(squaredic[i+1]):
            end.append(True)
        else:
            end.append(False)
    if set(squaredic[1]).intersection(squaredic[3]):
        end.append(True)
    else:
        end.append(False)
    if [(k, l, m) for k, l, m in itertools.product(squaredic[i-1], squaredic[i], squaredic[i+1]) if k < l < m]:
        end = [True, True, True]
    if not all(end):
        end = []
        for i in range(4, 6):
            if set(squaredic[i]).intersection(squaredic[i+1]):
                end.append(True)
            else:
                end.append(False)
        if set(squaredic[4]).intersection(squaredic[6]):
            end.append(True)
        else:
            end.append(False)
        if [(k, l, m) for k, l, m in itertools.product(squaredic[i-1], squaredic[i], squaredic[i+1]) if k < l < m]:
            end = [True, True, True]
    if not all(end):
        end = []
        for i in range(7, 9):
            if set(squaredic[i]).intersection(squaredic[i+1]):
                end.append(True)
            else:
                end.append(False)
        if set(squaredic[7]).intersection(squaredic[9]):
            end.append(True)
        else:
            end.append(False)
        if [(k, l, m) for k, l, m in itertools.product(squaredic[i-1], squaredic[i], squaredic[i+1]) if k < l < m]:
            end = [True, True, True]
    if not all(end):
        end = []
        for i in range(1, 9, 4):
            if set(squaredic[i]).intersection(squaredic[i+4]):
                end.append(True)
            else:
                end.append(False)
        if set(squaredic[1]).intersection(squaredic[9]):
            end.append(True)
        else:
            end.append(False)
        if [(k, l, m) for k, l, m in itertools.product(squaredic[i-4], squaredic[i], squaredic[i+4]) if k < l < m]:
            end = [True, True, True]
    if not all(end):
        end = []
        for i in range(3, 7, 2):
            if set(squaredic[i]).intersection(squaredic[i+2]):
                end.append(True)
            else:
                end.append(False)
        if set(squaredic[3]).intersection(squaredic[7]):
            end.append(True)
        else:
            end.append(False)
        if [(k, l, m) for k, l, m in itertools.product(squaredic[i-2], squaredic[i], squaredic[i+2]) if k < l < m]:
            end = [True, True, True]
    if not all(end):
        end = []
        for i in range(1, 7, 3):
            if set(squaredic[i]).intersection(squaredic[i+3]):
                end.append(True)
            else:
                end.append(False)
        if set(squaredic[1]).intersection(squaredic[7]):
            end.append(True)
        else:
            end.append(False)
        if [(k, l, m) for k, l, m in itertools.product(squaredic[i-3], squaredic[i], squaredic[i+3]) if k < l < m]:
            end = [True, True, True]
    if not all(end):
        end = []
        for i in range(2, 8, 3):
            if set(squaredic[i]).intersection(squaredic[i+3]):
                end.append(True)
            else:
                end.append(False)
        if set(squaredic[2]).intersection(squaredic[8]):
            end.append(True)
        else:
            end.append(False)
        if [(k, l, m) for k, l, m in itertools.product(squaredic[i-3], squaredic[i], squaredic[i+3]) if k < l < m]:
            end = [True, True, True]
    if not all(end):
        end = []
        for i in range(3, 9, 3):
            if set(squaredic[i]).intersection(squaredic[i+3]):
                end.append(True)
            else:
                end.append(False)
        if set(squaredic[3]).intersection(squaredic[9]):
            end.append(True)
        else:
            end.append(False)
        if [(k, l, m) for k, l, m in itertools.product(squaredic[i-3], squaredic[i], squaredic[i+3]) if k < l < m]:
            end = [True, True, True]
    return all(end)


round_list = []
for i in range(101):
    squaredic = {}
    small = [1 for _ in range(1, 10)]
    medium = [2 for _ in range(1, 10)]
    large = [3 for _ in range(1, 10)]
    steps = []
    ran_choice = ["small", "medium", "large"]
    for i in range(1, 10):
        squaredic[i] = []

    round = 0
    while not check_game_over(squaredic):
        place = random.randint(1, 9)
        piece = random.choice(ran_choice)

        if piece == "small" and small:
            if 1 not in squaredic[place]:
                round += 1
                squaredic[place].append(small.pop())

        if piece == "medium" and medium:
            if 2 not in squaredic[place]:
                round += 1
                squaredic[place].append(medium.pop())

        if piece == "large" and large:
            if 3 not in squaredic[place]:
                round += 1
                squaredic[place].append(large.pop())

    round_list.append(round)

print(sum(round_list)/len(round_list))
