# cook your dish here


def conv(l): # returns OR
    subs = [] 
    for i in range(len(l)):
        for j in range(i+1,len(l)+1):
            s = l[i: j]
            ands = s[0]
            for k in range(1, len(s)):
                ands = ands&s[k]
            subs.append(ands)
    # OR
    ors = subs[0]
    for i in range(len(subs)):
        ors = ors | subs[i]
    return ors


for _ in range(int(input())):
    N, Q = map(int, input().split())
    A = list(map(int, input().split()))
    B = []

    for i in range(Q):
        B.append(tuple(map(int, input().split())))

    print(conv(A))
    for i in range(Q):
        A[B[i][0]-1] = B[i][1]
        print(conv(A))

