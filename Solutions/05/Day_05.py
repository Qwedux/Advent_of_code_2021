import numpy as np
input_file ="input.txt"

with open(input_file) as inp:
    data = list(map(lambda s: [[int(coord) for coord in point.split(',')] for point in s.split(" -> ")] , inp.read().split('\n')))
    data = np.array(list(filter(lambda line: line[0][0] == line[1][0] or line[0][1] == line[1][1] or np.abs(line[1][0] - line[0][0]) == np.abs(line[1][1] - line[0][1]), data)))
    dirs = [(lambda line: (line[1] - line[0]) // np.gcd.reduce(line[1] - line[0]))(line) for line in data]
    used = dict()
    for index in range(data.shape[0]):
        for t in range(0, np.max(np.abs(data[index][1] - data[index][0])) // np.max(np.abs(dirs[index])) + 1):
            if str(data[index][0] + t * dirs[index]) in used.keys():
                used[str(data[index][0] + t * dirs[index])] += 1
            else:
                used[str(data[index][0] + t * dirs[index])] = 1
    print(len(list(filter(lambda elem: elem[1] > 1, used.items()))))
