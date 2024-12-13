import random

def random_direction_walk(length=1000, x=0, y=0):
    path = [(x, y)]

    for _ in range(length):
        dx, dy = random.choice([(1, 0), (-1, 0), (0, 1), (0, -1)])
        x, y = x + dx, y + dy
        path.append((x, y))

    return path