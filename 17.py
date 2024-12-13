import random

def random_ten():
    nums = random.sample(range(1, 101), 10)
    return min(nums), max(nums)