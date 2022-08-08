from queue import PriorityQueue
import numpy as np
input_file ="sample.txt" if 0 else "input.txt"

with open(input_file) as inp:
    grid = np.array([list(map(int, list(row))) for row in inp.read().split('\n')])
    grid = np.array([np.append(row, [row+1, row+2, row+3, row+4]) for row in grid])
    grid = np.vstack((grid, grid+1, grid+2, grid+3, grid+4))
    grid = ((grid-1) % 9) + 1
    # print(grid)
    # exit()
    moves = [(0,-1),(0,1),(-1,0),(1,0)]
    visited = set([])
    distances = [[123456789123456789 for _ in row] for row in grid]
    came_from = [[-1 for _ in row] for row in grid]
    # print(*grid, sep='\n')

    pq = PriorityQueue()
    pq.put(((0, -1), (0,0)))
    
    while not pq.empty():
        (dist, where_from), (r,c) = pq.get()
        if (r,c) in visited:
            continue
        visited.add((r,c))
        distances[r][c] = dist
        came_from[r][c] = where_from
        for i, (dr, dc) in zip(range(len(moves)), moves):
            if r+dr >= 0 and r+dr < len(grid) and c+dc >= 0 and c+dc < len(grid[0]):
                pq.put(((dist+grid[r+dr][c+dc], i), (r+dr, c+dc)))

    proc = [-1,-1]
    while proc:
        r, c = proc[0], proc[1]
        if came_from[r][c] != -1:
            proc = [r-moves[came_from[r][c]][0], c-moves[came_from[r][c]][1]]
        else:
            proc = []
        came_from[r][c] = 4
    print(distances[-1][-1])
    # print(*came_from,sep='\n')
