# BUYPLSE
a, b, x, y = map(int, input().split())
print(a*x + b*y)

# ISBOTH
N = int(input())
if N%55==0:
    print("BOTH")
elif N%5 == 0 or N%11 == 0:
    print("ONE")
else:
    print("NONE")

# DIFACTRS
n = int(input())

fact = []

for i in range(1, n+1):
    if n%i == 0:
        fact.append(i)

print(len(fact))
s = " ".join(map(str, fact))
print(s)

# SECLAR
n = 3
nums = []
while n != 0:
    nums.append(int(input()))
    n -= 1

nums.sort()
print(nums[-2])

# RNGEODD
L, R = map(int, input().split())

while L <= R:
    if L%2 != 0:
        print(L, end = " ")
    L += 1

# VALTRI
n = int(input())

if n%5 == 0 or n%6 == 0:
    print("YES")
else:
    print("NO")

# FINDMELI
_, K = map(int, input().split())

tp = tuple(map(int, input().split()))

if K in tp:
    print(1)
else:
    print(-1)
    
# REVMEE
_ = input()

tp = tuple(map(int, input().split()))

for i in tp[::-1]:
    print(i, end = " ")
    

