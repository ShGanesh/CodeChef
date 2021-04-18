# cook your dish here
for _ in range(int(input())):
    n, x = map(int, input().split())
    c = tuple(map(int, input().split()))
    chocs = []
    for i in set(c):
        chocs.append([i, c.count(i)])

    for j in chocs:
        while j[1] > 1:
            if x > 0:
                j[1] -= 1
                x -= 1
            else:
                break
    

    if x != 0:
        print(len(chocs)-x)
    else:
        ava = 0
        for k in chocs:
            if k[1] != 0:
                ava += 1
        print(ava)
