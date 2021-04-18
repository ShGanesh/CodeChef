# cook your dish here
_ = input()
l = tuple(map(int, input().split()))

count = 0
for i in l:
    if i%2==0:
        count += 1
    else:
        count -= 1

print("READY FOR BATTLE") if count > 0 else print("NOT READY")
    
