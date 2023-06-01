for i in range(int(input())):
    a = list(map(int, input().split()))
    del a[0]
    c = 0
    for b in a:
        if b > sum(a)/len(a):
            c += 1
    print('{:.3f}%'.format(100*c/len(a)))
