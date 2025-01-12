t = int(input()) # number of test cases
for i in range(t):
    n, k =  map(int, input().split()) # number of ppl and threshold
    ind_gold = list(map(int, input().split())) # individual gold of ppl
    num_ppl = 0
    curr_gold = 0 # if a_i >= k take all gold, if a_i == 0, give 1 gold
    for i in range(len(ind_gold)):
        if ind_gold[i] >= k:
            curr_gold += ind_gold[i]
            ind_gold[i] = 0
        elif ind_gold[i] == 0 and curr_gold >= 1:
            curr_gold -= 1
            ind_gold[i] += 1
            num_ppl += 1
        else: 
            continue
    print(num_ppl)