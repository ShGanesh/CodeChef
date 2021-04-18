# cook your dish here
for _ in range(int(input())):
    B = int(input())
    if B == 1 or B == 2 or B == 3:
        print(0)
    else:
        if B%2 == 0:
            print(sum(range(int(B/2))))
        else:
            print(sum(range(int((B-1)/2))))
        
