from collections import defaultdict
input_file ="sample.txt" if 0 else "input.txt"

with open(input_file) as inp:
    s_pos = [int(row.split(' ')[-1]) for row in inp.read().split('\n')]
    # print(s_pos)

    # part 1
    # def step(pol, dice):
    #     return (pol-1+3*dice+3)%10+1, dice + 3
    
    # score_1, score_2 = 0,0
    # dice = 1
    # while score_1 < 1000 and score_2 < 1000:
    #     s_pos[0], dice = step(s_pos[0], dice)
    #     score_1 += s_pos[0]
    #     if score_1 >= 1000:
    #         print(score_2 * (dice-1))
    #         break
    #     s_pos[1], dice = step(s_pos[1], dice)
    #     score_2 += s_pos[1]
    #     if score_2 >= 1000:
    #         print(score_1 * (dice-1))
    #         break

    # part 2
    states = defaultdict(lambda : 0)
    states[(s_pos[0], s_pos[1], 0, 0)] = 1
    w_1, w_2 = 0, 0
    def step(states, player):
        res = defaultdict(lambda : 0)
        p_1 = 0
        p_2 = 0
        if player == 0:
            for key in states:
                for roll, freq in {3:1, 4:3, 5:6, 6:7, 7:6, 8:3, 9:1}.items():
                    if key[2] + (key[0]-1+roll)%10+1 >= 21:
                        p_1 += freq * states[key]
                    else:
                        res[((key[0]-1+roll)%10+1, key[1], key[2] + (key[0]-1+roll)%10+1, key[3])] += freq * states[key]
        else:
            for key in states:
                for roll, freq in {3:1, 4:3, 5:6, 6:7, 7:6, 8:3, 9:1}.items():
                    if key[3] + (key[1]-1+roll)%10+1 >= 21:
                        p_2 += freq * states[key]
                    else:
                        res[(key[0], (key[1]-1+roll)%10+1, key[2], key[3] + (key[1]-1+roll)%10+1)] += freq * states[key]
        return res, p_1, p_2
    
    player = 0
    while states:
        tmp = step(states, player=player)
        player = 1 - player
        states = tmp[0]
        w_1 += tmp[1]
        w_2 += tmp[2]
    
    print(w_1, w_2)