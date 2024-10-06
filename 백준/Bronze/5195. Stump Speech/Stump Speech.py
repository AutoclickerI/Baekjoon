R = input
for i in range(int(R())):
    print(f'Data Set {i+1}:')
    s=[(R(),int(R()))for _ in range(int(R()))]
    c=R()
    r=0
    for i in range(len(c)):
        for t,u in s:
            if c[i:i+len(t)]==t:r+=u
    print(r)