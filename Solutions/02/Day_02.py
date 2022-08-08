from operator import add

input_file = "inp.txt"

with open(input_file) as inp:
    data = inp.read().split('\n')[:-1]
    data = [(lambda x: (x[0], int(x[1])))(dato.split(" ")) for dato in data]
    res = [0,0]
    for index in range(len(data)):
        res = list(map(add, res, {
            'forward': lambda x: [x,0],
            'down': lambda x: [0,x],
            'up': lambda x: [0,-x],
        }[data[index][0]](data[index][1])
        ))
    print(res[0] * res[1])
    
    res = [0,0,0]
    for index in range(len(data)):
        res = {
            'forward': lambda x, y: [x[0]+y, x[1] + y*x[2], x[2]],
            'down': lambda x, y: [x[0], x[1], x[2]+y],
            'up': lambda x, y: [x[0], x[1], x[2]-y],
        }[data[index][0]](res, data[index][1])
    print(res[0] * res[1])
    