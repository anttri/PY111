import numpy as np


def sort(data, min, max):
    n = max - min + 1

    counters = [0] * n
    for m in data:
        counters[m - min] += 1

    result = []
    for p, count in enumerate(counters):
        result.extend([p + min] * count)

    return result


if __name__ == "__main__":
    N = 10 ** 6
    arr = np.random.randint(13, 26, N)

    print(arr[:20])
    print(sort(arr, 13, 26)[:15])
