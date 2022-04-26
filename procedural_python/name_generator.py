import random


def dragon_name(fname, mob):
    combined = fname+mob
    to_random = list(combined)
    random.shuffle(to_random)
    result = ''.join(to_random)
    return result


def penguin_name(fname, mob):
    combined = mob+fname+'noot'
    to_random = list(combined)
    random.shuffle(to_random)
    result = ''.join(to_random)
    return result
