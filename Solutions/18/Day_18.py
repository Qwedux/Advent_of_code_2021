input_file ="sample.txt" if 0 else "input.txt"

# def generate_all_trees(d):
#     if d == 0:
#         return [[]]
#     else:
#         res = [[]]
#         tmp = generate_all_trees(d-1)
#         for sub_t1 in tmp:
#             res.append([sub_t1])
#             for sub_t2 in tmp:
#                 res.append([sub_t1, sub_t2])
#         return res

# def nodes(tree):
#     res = 1

#     for sub_t in range(len(tree)):
#         res += nodes(tree[sub_t])
#     return res

# print(list(map(nodes, generate_all_trees(3))))

def reduce_number(number):
    depth = 0
    index = 0
    while index < len(number):
        if number[index] == '[':
            depth += 1
            if depth > 4:
                # DONE: explode!
                ind_copy = index
                while ind_copy >= 0:
                    if str(number[ind_copy]).isdigit():
                        number[ind_copy] += number[index+1]
                        break
                    ind_copy -= 1
                ind_copy = index + 3
                while ind_copy < len(number):
                    if str(number[ind_copy]).isdigit():
                        number[ind_copy] += number[index+2]
                        break
                    ind_copy += 1
                number = number[:index] + [0] + number[index+4:]
                return number, True
        elif number[index] == ']':
            depth -= 1
        index += 1
    index = 0
    while index < len(number):
        if str(number[index]).isdigit() and number[index] >= 10:
            # DONE: you got number
            number = number[:index] + ['[', number[index] // 2, number[index] // 2 + number[index] % 2, ']']+ number[index+1:]
            return number, True
        index += 1
    return number, False

def reduced(number, debug):
    fancyprint(number, debug)
    while True:
        number, done = reduce_number(number)
        fancyprint(number, debug)
        if not done:
            break
    return number

def add_numbers(a, b, debug):
    res = ['['] + a + b + [']']
    return reduced(res, debug)

def magnitude(number):
    stack = []
    index = 0
    while index < len(number):
        if number[index] == ']':
            stack = stack[:-2] + [3*stack[-2] + 2*stack[-1]]
        elif type(number[index]) == int:
            stack += [number[index]]
        index += 1
    return stack

def fancyprint(number, deb):
    if not deb:
        return
    index = 0
    stack = [False]
    while index < len(number):
        if number[index] == '[':
            stack += [True]
            print('[', end='')
        else:
            print(number[index], end='')
            comma = stack.pop()
            if comma:
                print(',', end='')
                stack += [False]
        index += 1
    print()

with open(input_file) as inp:
    debug = False
    numbers = inp.read().split("\n")
    numbers = [[x if x in "[]" else int(x) for x in number if x != ','] for number in numbers]

    res = reduced(numbers[0], debug)
    index = 1
    while index < len(numbers):
        res = add_numbers(res, numbers[index], debug)
        index += 1
        
    # fancyprint(res, True)
    print(magnitude(res))
    print(max([max([magnitude(add_numbers(a, b, debug)) for b in numbers if a != b]) for a in numbers]))