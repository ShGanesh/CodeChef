# cook your dish here
lead = 0
winner = 0
a = 0
b = 0

for i in range(int(input())):
    x, y = map(int, input().split())
    a += x
    b += y
    if a - b > lead:
        winner = 1
        lead = a - b
    elif b - a > lead:
        winner = 2
        lead = b - a

print(winner, lead)
