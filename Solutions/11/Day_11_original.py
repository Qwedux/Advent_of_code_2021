import numpy as np
input_file ="sample.txt" if 0 else "input.txt"

with open(input_file) as inp:
    data = np.array([[int(cell) for cell in row] for row in inp.read().split('\n')])

    def increment(a, b):
        a[:-1] += b[1:]
        a[1:] += b[:-1]
        a[:, :-1] += b[:, 1:]
        a[:, 1:] += b[:, :-1]
        a[:-1, :-1] += b[1:, 1:]
        a[:-1, 1:] += b[1:, :-1]
        a[1:, :-1] += b[:-1, 1:]
        a[1:, 1:] += b[:-1, :-1]

    def update(arr):
        arr += 1
        ready, was_ready  = np.array(arr > 9, dtype=int), np.zeros_like(arr, dtype=int)
        while np.any(ready == 1):
            increment(arr, ready)
            was_ready += ready
            ready = np.array(arr > 9, dtype=int) - np.array(was_ready > 0, dtype=int)
        arr *= 1 - np.array(was_ready > 0, dtype=int)
        return np.sum(was_ready)

    # # part 1
    # print(sum([update(data) for _ in range(100)]))

    # part 2
    steps = 0
    while np.any(data != 0): 
        steps, _ = steps+1, update(data)
    print(steps)