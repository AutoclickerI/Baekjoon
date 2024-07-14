for s in[*open(0)][2::2]:
    a=0
    t=[]
    for j,i in enumerate(s):
        if'H'<i:t+=j,
        if 1<len(t)and t[-1]-t[-2]&1:a+=t[-1]-t[-2];t.pop();t.pop()
    print(-1 if t else a)