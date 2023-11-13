for n in[*map(int,open(0))][1:]:
    l=[0]*n
    for i in range(n):
        j=i
        while j<n:
            l[j]^=1
            j+=i+1
    print(sum(l))