input_file ="sample.txt" if 0 else "input.txt"

with open(input_file) as inp:
    data = inp.read().split('\n')
    def corrupted(line):
        tmp = []
        opposite = {')':'(', ']':'[', '}':'{', '>':'<'}
        scoring = {')':3, ']':57, '}':1197, '>':25137}
        for char in line:
            if char in '([{<':
                tmp.append(char)
            elif opposite[char] != tmp[-1]:
                return scoring[char]
            else:
                tmp.pop()
        return 0
    def autocomplete(line):
        tmp = []
        score = 0
        scoring = {'(':1, '[':2, '{':3, '<':4}
        for char in line:
            if char in '([{<':
                tmp.append(char)
            else:
                tmp.pop()
        tmp.reverse()
        for char in tmp:
            score *= 5
            score += scoring[char]
        return score

    # part one
    print(sum(filter(lambda x: x != 0, [corrupted(line) for line in data])))
    completed = [autocomplete(line) for line in [line for line in data if corrupted(line) == 0]]
    # part two
    print(sorted(completed)[len(completed)//2])
    