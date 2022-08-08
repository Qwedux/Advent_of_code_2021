from collections import namedtuple
from math import floor, ceil
input_file ="sample.txt" if 0 else "input.txt"

with open(input_file) as inp:
    target_area = list(map(int, filter(None, (''.join([c if c != ' ' else '.' for c in inp.read() if c.isdigit() or c == '-' or c == '.' or c == ' '])).split('.'))))
    # print(target_area)
    target_area = namedtuple('Limits', ['x', 'y'])(namedtuple('Range', ['min', 'max'])(target_area[0], target_area[1]), namedtuple('Range', ['min', 'max'])(target_area[2], target_area[3]))
    print(target_area)
    def step(posx, posy, dx, dy):
        return (posx+dx, posy+dy, dx-1 if dx > 0 else 0, dy-1)

    def simulate(x, y, target_area):
        sx, sy = 0, 0
        highst_y = 0
        while sx <= target_area.x.max and sy >= target_area.y.min:
            sx, sy, x, y = step(sx, sy, x, y)
            highst_y = max(highst_y, sy)
            if sx <= target_area.x.max and sx >= target_area.x.min and sy <= target_area.y.max and sy >= target_area.y.min:
                return highst_y, True
        return 0, False
    
    h_hit = 0
    init_vels = []
    # print(init_vels)
    for x in range(target_area.x.max+1):
        for y in range(target_area.y.min, abs(target_area.y.min)):
            hishest_hit, hit = simulate(x,y, target_area)
            if hit:
                # print(x,y,hishest_hit)
                h_hit = max(h_hit, hishest_hit)
                # print((x,y))
                init_vels.append((x,y))
    print(h_hit)
    print(len(sorted(list(set(init_vels)))))
    # def x_after_k(x, k):
    #     if k >= x+1:
    #         return (x*(x+1))//2
    #     else:
    #         return (k*(2*x+1-k))//2

    # possible_starting_vels = set([])
    # for k in range(1, 5000):
    #     if ceil((target_area.y.min + (k*(k-1))//2)/k) !=  floor((target_area.y.max + (k*(k-1))//2)/k)+1:
    #         for x in range(1, 222):
    #             possible_starting_vels.update(
    #                 [(x, dy) for dy in range(ceil((target_area.y.min + (k*(k-1))//2)/k), floor((target_area.y.max + (k*(k-1))//2)/k)+1) if target_area.x.min <= x_after_k(x, k) and target_area.x.max >= x_after_k(x, k)]
    #                 )
    # possible_starting_vels = sorted(list(possible_starting_vels))
    # print(sorted(list(set([(x, y) for x, y in possible_starting_vels if y >= 0]))))
    # heights = sorted(list(set([(y*(y-1))//2 for _, y in possible_starting_vels if y >= 0])))
    # print(heights[-1])
