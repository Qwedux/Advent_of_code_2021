input_file = "inp.txt"

with open(input_file) as inp:
    data = inp.read().split('\n')[:-1]
    data = [[int(x) for x in dato] for dato in data]
    gamma = [1 if 2*sum(x) >= len(data) else 0 for x in zip(*data)]
    epsilon = [1 if gamma[index] == 0 else 0 for index in range(len(gamma))]
    def convert_to_decimal(arr):
        pows = [2**i for i in range(len(gamma)-1, -1, -1)]
        return sum([arr[index] * pows[index] for index in range(len(arr))])

    print(convert_to_decimal(gamma) * convert_to_decimal(epsilon))

    def dominant(arr, index):
        return 1 if 2*sum([dato[index] for dato in arr]) >= len(arr) else 0
    
    def compute_rating(data, mode):
        rating, ind = data, 0
        while len(rating) > 1:
            dom = dominant(rating, ind)
            rating, ind = [dato for dato in rating if (dato[ind] == dom) == mode], ind+1
        return rating[0]
    
    print(convert_to_decimal(compute_rating(data, 1)) * convert_to_decimal(compute_rating(data, 0)))
