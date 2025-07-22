for i in[*open(0)][1:]:
    a=[i[0]]
    x=[]
    v=0
    for c in i:
        f=a[-1]==c
        if f:v+=1
        else:a+=c,;x+=v,;v=1
    for i,j in zip(a,x):print(j,i)