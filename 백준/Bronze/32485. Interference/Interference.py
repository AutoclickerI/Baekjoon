waves=[]
for q,*v in[i.split()for i in[*open(0)]][1:]:
    if q=='?':
        h=0
        v=int(v[0])
        for p,l,a in waves:
            if p<=v<p+l:
                if(v-p)%4==0:
                    h+=a
                if(v-p)%4==2:
                    h-=a
        print(h)
    else:
        waves+=tuple(map(int,v)),