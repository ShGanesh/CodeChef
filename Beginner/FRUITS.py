# cook your dish here
for _ in range(int(input())):
    A, O, K = map(int, input().split())
    diff = abs(A-O)
    if K >= diff:
        print(0)
    else:
        print(diff-K)
