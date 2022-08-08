from collections import Counter
input_file ="sample.txt" if 0 else "input.txt"

with open(input_file) as inp:
    polymer, _, *insertion_rules  = inp.read().split('\n')
    insertion_rules = dict((lambda x: (x[0], x[2]))(rule.split()) for rule in insertion_rules)
    letter_counts = Counter([a for a in polymer])
    pair_counts = Counter([a+b for a,b in zip(polymer, polymer[1:])])
    
    def update(l_cnt, p_cnt, rules):
        res_p_cnt = Counter()
        for pair, cnt in p_cnt.items():
            if pair in rules:
                new_letter = rules[pair]
                res_p_cnt[pair[0]+new_letter] += cnt
                res_p_cnt[new_letter+pair[1]] += cnt
                l_cnt[new_letter] += cnt
        return l_cnt, res_p_cnt
    
    for N in [10,40]:
        for _ in range(N):
            letter_counts, pair_counts = update(letter_counts, pair_counts, insertion_rules)
        print(letter_counts.most_common()[0][1] - letter_counts.most_common()[-1][1])