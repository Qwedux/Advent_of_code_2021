input_file ="input.txt"

with open(input_file) as inp:
    data = list(map(int, inp.read().split(',')))
    res1 = sum([abs(elem - min(data)) for elem in data])
    res2 = sum([abs(elem - min(data))*(abs(elem - min(data)) + 1)//2 for elem in data])
    for x in range(min(data), max(data)+1):
        res1 = min(res1, sum([abs(elem - x) for elem in data]))
        res2 = min(res2, sum([abs(elem - x)*(abs(elem - x) + 1)//2 for elem in data]))
    print(res1, res2)
