# cook your dish here
for _ in range(int(input())):
    Am, Bm, Cm, Tm, A, B, C = map(int, input().split())
    if (Am <= A) and (Bm <= B) and (Cm <= C):
        if (A + B + C) >= Tm:
            print("YES")
        else: print("NO")
    else: print("NO")
