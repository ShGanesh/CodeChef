
# cook your dish here
for _ in range(int(input())):
    #print("NEW")
    N, R = map(int, input().split())
    #print(N, R)
    A = tuple(map(int, input().split()))
    B = tuple(map(int, input().split()))
    #print(A, B)
    t,s = 0, 1
    fa_pk = [t]
    for i in range(N-1):
        #print("Entered loop.")
        s = A[i+1] - A[i]
        #print("d(A):", A[i+1], A[i])
        t += B[i]
        fa_pk.append(t)
        t -= R*s
        fa_pk.append(t)
        #print("i =", i, ", d(A) =", s, " Current Tension = ", t)
    t += B[-1]
    fa_pk.append(t)
    fa_pk.sort()
    print(fa_pk)
    print(fa_pk[-1])
