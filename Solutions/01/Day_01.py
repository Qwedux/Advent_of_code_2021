with open("input.txt") as inp:
    data = inp.read().split('\n')[:-1]
    data = [int(x) for x in data]
    print(sum([data[index-1] < data[index] for index in range(1, len(data))]))

    data = [x+y+z for x,y,z in zip(data, data[1:], data[2:])]
    # print(data)
    print(sum([data[index-1] < data[index] for index in range(1, len(data))]))