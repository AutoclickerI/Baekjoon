for i in[*open(0)][:-1]:
    s=c=t=''
    for j in i:
        if j!=t:s+=f'{c}{t}';c=0;t=j
        c+=1
    print(s)