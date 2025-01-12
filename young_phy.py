# def myfunc(a, b):
#   return a + b
# x = map(myfunc, ('apple', 'banana', 'cherry'), ('orange', 'lemon', 'pineapple'))
# print(list(x))

n = int(input())
xSum = 0 
ySum = 0
zSum = 0
for i in range(n):
    # Apply int function to split input values the stored in x, y, z
    x, y, z = map(int, input().split())
    xSum += x
    ySum += y
    zSum +=z 
    
if xSum ==0 and ySum ==0 and zSum ==0:
    print("YES")
else:
    print("NO")
        