from numpy import *
from itertools import *
input_file ="sample.txt" if 0 else "input.txt"

with open(input_file) as inp:
    data = array([[int(cell) for cell in row] for row in inp.read().split('\n')])

    def increment(a, b):
        m = array([[0,-1, 1, a.shape[0]], [1, a.shape[0], 0, -1], [0, a.shape[0], 0, a.shape[0]]])
        for r, c in list(product(range(3), range(3))):
            if (r != 2 or c != 2):
                a[m[r, 0]:m[r, 1], m[c, 0]:m[c, 1]] += b[m[r, 2]:m[r, 3], m[c, 2]:m[c, 3]]
    
    def update(arr):
        arr += 1
        ready, was_ready  = arr > 9, zeros_like(arr, dtype=bool)
        while any(ready == 1):
            was_ready, _, ready = was_ready + ready, increment(arr, ready), (arr > 9) ^ ((was_ready + ready) > 0)
        arr *= 1 - (was_ready > 0)
        return sum(was_ready)

    # # part 1
    # print(sum([update(data) for _ in range(100)]))

    # part 2
    steps = 0
    while any(data != 0): 
        steps, _ = steps+1, update(data)
    print(steps)