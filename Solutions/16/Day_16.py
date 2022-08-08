import math
input_file ="sample.txt" if 0 else "input.txt"

versions = 0
with open(input_file) as inp:
    preloz = {
        '0' : '0000',
        '1' : '0001',
        '2' : '0010',
        '3' : '0011',
        '4' : '0100',
        '5' : '0101',
        '6' : '0110',
        '7' : '0111',
        '8' : '1000',
        '9' : '1001',
        'A' : '1010',
        'B' : '1011',
        'C' : '1100',
        'D' : '1101',
        'E' : '1110',
        'F' : '1111'
    }
    hexadec = ''.join([preloz[x] for x in inp.read()])
    print(hexadec)

    def parse(inp):
        if all(x == '0' for x in inp):
            return None, ""
        version, type = int(inp[:3], 2), int(inp[3:6], 2)
        val = inp[6:]
        global versions
        versions += version
        print('VVVTTT', end='')

        if type == 4:
            num = ""
            while val[0] == '1':
                print("AAAAA", end='')
                num += val[1:5]
                val = val[5:]
            print("AAAAA", end='')
            num += val[1:5]
            val = val[5:]
            return int(num, 2), val
        else:
            res = []
            print("I", end='')
            if val[0] == '0':
                # 15 bits length
                print("LLLLLLLLLLLLLLL", end='')
                count = int(val[1:1+15], 2)
                tmp, rem = parse(val[1+15:1+15+count])
                while tmp != None:
                    res.append(tmp)
                    tmp, rem = parse(rem)
                val = val[1+15+count:]
            else:
                # num of subpackets
                print("LLLLLLLLLLL", end='')
                count = int(val[1:1+11], 2)
                val = val[1+11:]
                for _ in range(count):
                    tmp, val = parse(val)
                    res.append(tmp)
            if type == 0:
                return sum(res), val
            elif type == 1:
                return math.prod(res), val
            elif type == 2:
                return min(res), val
            elif type == 3:
                return max(res), val
            elif type == 5:
                return 1 if res[0] > res[1] else 0, val
            elif type == 6:
                return 1 if res[0] < res[1] else 0, val
            elif type == 7:
                return 1 if res[0] == res[1] else 0, val
            return res, val
    res, _ = parse(hexadec)
    print()
    print(res)
    print(versions)
