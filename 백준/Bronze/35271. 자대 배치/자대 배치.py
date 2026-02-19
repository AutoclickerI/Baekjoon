[N,M],c,*l=[[*map(int,i.split())]for i in open(0)]

for i in l:
    for v in i:
        if c[v-1]:
            c[v-1]-=1
            print(v)
            break
    else:
        print(-1)