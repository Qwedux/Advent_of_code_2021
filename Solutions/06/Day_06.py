input_file ="input.txt"

with open(input_file) as inp:
    data = inp.read().split(',')
    data = [data.count(str(i)) for i in range(9)]
    def iter(fish):
        new_fish = [0 for _ in range(9)]
        for f in range(8,-1,-1):
            if f != 0:
                new_fish[f-1] = fish[f]
            else:
                new_fish[6] += fish[0]
                new_fish[8] = fish[0]
        return new_fish
    for _ in range(80):
        data = iter(data)
    print(sum(data))
