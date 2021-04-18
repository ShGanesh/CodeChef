# cook your dish here
for _ in range(int(input())):
    n = int(input())
    l = 0
    d = 1
    while n > 0:
        n -= d
        d += 1
        l += 1
    
    if n < 0:
        print(l-1)
    else: print(l)
