import random
t = int(input())
lst = []
for i in range(t):
    s = input()
    lst.append(s)

for i in lst:
    lst_set = set()
    s = ""
    s += i
    for j in s:
        if j not in lst_set:
            lst_set.add(j)
        else:
            continue
    if len(lst_set) > 1:
        print("YES")
        while(True):
            rand_int = random.randint(1, len(s)-1)
            r = s[rand_int:]+s[:rand_int]
            if r != s:
                print(r)
                break
    else:
        print("NO")
