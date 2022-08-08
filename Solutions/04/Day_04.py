import numpy as np
input_file ="input.txt"

with open(input_file) as inp:
    drawn_numbers, *tables = inp.read().split('\n\n')
    drawn_numbers = [int(num) for num in drawn_numbers.split(',')]
    tables = [[[int(num) for num in (' '.join(row.split())).split(' ')] for row in table.split('\n')] for table in tables]
    tables = np.array(tables)
    drawn = np.zeros_like(tables, dtype=int)

    def col_check(a):
        winning_boards = []
        for index in range(a.shape[0]):
            for col in range(a.shape[2]):
                if np.sum(a[index, :, col]) == a.shape[1]:
                    winning_boards.append(index)
                    break
        return winning_boards
    
    def row_check(a):
        winning_boards = []
        for index in range(a.shape[0]):
            for row in range(a.shape[1]):
                if np.sum(a[index, row]) == a.shape[2]:
                    winning_boards.append(index)
                    break
        return winning_boards

    def mark(a, b, str):
        for index in range(len(a)):
            for row_ind in range(len(a[index])):
                for col_ind in range(len(a[index][row_ind])):
                    if b[index][row_ind][col_ind] == str:
                        a[index][row_ind][col_ind] = 1
        return list(set(row_check(a) + col_check(a)))
        
    finished, drawing, prev_winers = False, 0, []
    while not finished:
        winners = mark(drawn, tables, drawn_numbers[drawing])
        if len(winners) >= drawn.shape[0]:
            winner = list(set(winners) - set(prev_winers))[0]
            print(np.sum(tables[winner] * (1-drawn[winner])) * drawn_numbers[drawing])
            break
        prev_winers = winners
        drawing += 1
    # print(drawn)
    
