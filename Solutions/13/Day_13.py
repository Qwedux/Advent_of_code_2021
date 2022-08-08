import numpy as np
input_file ="sample.txt" if 0 else "input.txt"

with open(input_file) as inp:
    data  = inp.read().split('\n')
    dots = np.array([[int(x) for x in row.split(',')] for row in data if row[:1].isdigit()])
    instr = [r.split(' ')[-1].split('=') for r in data if r[:1] == 'f']

    grid = np.zeros((np.max(dots[:, 1])+1, np.max(dots[:, 0])+1), dtype=int)
    for r in dots:
        grid[r[1], r[0]] = 1

    def fold_x(arr, x):
        fp, sp = arr[:, :x], arr[:, x+1:2*x+1]
        fp[:, :sp.shape[1]] += np.flip(sp, axis=1)
        return fp
    def fold_y(arr, y):
        fp, sp = arr[:y], arr[y+1:2*y+1]
        fp[:sp.shape[0]] += np.flip(sp, axis=0)
        return fp
    
    def fancy(arr):
        print('\n'.join([''.join(['.' if c == 0 else '#' for c in r]) for r in arr]))
    
    for inst in instr:
        if inst[0] == 'x':
            grid = fold_x(grid, int(inst[1]))
        else:
            grid = fold_y(grid, int(inst[1]))
        print(np.sum(grid > 0))
    fancy(grid)