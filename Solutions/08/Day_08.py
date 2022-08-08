input_file ="input.txt"

with open(input_file) as inp:
    data = inp.read().split('\n')
    res = [0 for _ in range(10)]
    outs = [[]]
    for inp, out in [x.split('|') for x in data]:
        inp, out = sorted([set(x) for x in inp.split()], key=len), [set(x) for x in out.split()]
        def count_letters(a):
            res = {'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'f': 0, 'g': 0}
            for dato in a:
                for letter in list(dato):
                    res[letter] += 1
            return res
        alls  = count_letters(inp)
        fives = count_letters(inp[3:6])
        sixes = count_letters(inp[6:9])
        for digit in out:
            if len(digit) == 2:
                res[1] += 1
                outs[-1].append("1")
            elif len(digit) == 3:
                res[7] += 1
                outs[-1].append("7")
            elif len(digit) == 4:
                res[4] += 1
                outs[-1].append("4")
            elif len(digit) == 7:
                res[8] += 1
                outs[-1].append("8")
            elif len(digit) == 5:
                letter_b = None
                letter_f = None
                for letter in "abcdefg":
                    if alls[letter] == 6 and fives[letter] == 1:
                        letter_b = letter
                    elif alls[letter] == 9:
                        letter_f = letter
                
                if letter_b in digit:
                    res[5] += 1
                    outs[-1].append("5")
                elif letter_f in digit:
                    res[3] += 1
                    outs[-1].append("3")
                else:
                    res[2] += 1
                    outs[-1].append("2")
            elif len(digit) == 6:
                letter_c = None
                letter_e = None
                for letter in "abcdefg":
                    if alls[letter] == 4:
                        letter_e = letter
                    elif alls[letter] == 8 and sixes[letter] == 2:
                        letter_c = letter
                if not letter_c in digit:
                    res[6] += 1
                    outs[-1].append("6")
                elif letter_e in digit:
                    res[0] += 1
                    outs[-1].append("0")
                else:
                    res[9] += 1
                    outs[-1].append("9")
        outs.append([])
    
    print(res[1] + res[4] + res[7] + res[8])
    print(sum([int(''.join(x)) for x in outs[:-1]]))