import numpy as np
from functools import reduce
from numpy.core.numeric import zeros_like
input_file ="sample.txt" if 0 else "input.txt"

with open(input_file) as inp:
    data = np.array([[int(cell) for cell in row] for row in inp.read().split('\n')])

    smaller = zeros_like(data)
    chck = np.zeros_like(data)
    smaller[:-1]    += data[:-1] < data[1:]       # upper cell is smaller then lower cell
    smaller[1:]     += data[1:] < data[:-1]       # lower cell is smaller then upper cell
    smaller[:, :-1] += data[:, :-1] < data[:, 1:] # left  cell is smaller then right cell
    smaller[:, 1:]  += data[:, 1:] < data[:, :-1] # right cell is smaller then left  cell

    chck[:-1]    += np.ones_like(chck[:-1])
    chck[1:]     += np.ones_like(chck[1:])
    chck[:, :-1] += np.ones_like(chck[:, :-1])
    chck[:, 1:]  += np.ones_like(chck[:, 1:])

    low_points = chck == smaller
    print(np.sum((data+1) * (low_points)))

    visited = np.zeros_like(data)
    def get_basin_size(r, c):
        if visited[r][c] or data[r][c] == 9:
            return 0
        visited[r][c] = 1
        res = 0
        if r > 0:
            res += get_basin_size(r-1, c)
        if c > 0:
            res += get_basin_size(r, c-1)
        if r+1 < visited.shape[0]:
            res += get_basin_size(r+1, c)
        if c+1 < visited.shape[1]:
            res += get_basin_size(r, c+1)
        return res + 1
    basins = []
    for r in range(low_points.shape[0]):
        for c in range(low_points.shape[1]):
            if low_points[r][c]:
                basins.append(get_basin_size(r, c))
    print(reduce(lambda x,y: x*y, sorted(basins)[-3:]))