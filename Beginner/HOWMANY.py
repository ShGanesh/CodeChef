# cook your dish here

t=int(input())

if t == 0:
    print(0)
else:
    if len(str(t)) > 3:
        print("More than 3 digits")
    else:
        print(len(str(t)))
