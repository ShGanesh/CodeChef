# cook your dish here
for _ in range(int(input())):
    N, K = map(int, input().split())
    rem = 0
    for i in range(1, K+1):
        if N%i > rem:
            rem = N%i
    print(rem)

    
