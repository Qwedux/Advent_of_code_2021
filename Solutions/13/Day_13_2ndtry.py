input_file ="sample.txt" if 0 else "input.txt"

with open(input_file) as inp:
    data  = inp.read().split('\n')
    dots = {tuple([int(x) for x in row.split(',')]):True for row in data if row[:1].isdigit()}
    instr = [r.split(' ')[-1].split('=') for r in data if r[:1] == 'f']
    for d, v in instr:
        v = int(v)
        G2 = {}
        if d == 'x':
            for (x,y) in dots:
                if x < v:
                    G2[(x,y)] = True
                else:
                    G2[(v-(x-v), y)] = True
        else:
            for (x,y) in dots:
                if y < v:
                    G2[(x,y)] = True
                else:
                    G2[(x, v-(y-v))] = True
        dots = G2
    X, Y = max([x for x,_ in dots]), max([y for _,y in dots])
    for y in range(Y+1):
        ans = ''
        for x in range(X+1):
            ans += ('#' if (x,y) in dots else ' ')
        print(ans)

    