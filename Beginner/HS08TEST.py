# cook your dish here
w, b = map(float, input().split())

if (w +0.5 > b) or (w%5 != 0):
    print("{0:.2f}".format(b))
else:
    print("{0:.2f}".format(b-w-0.5))
