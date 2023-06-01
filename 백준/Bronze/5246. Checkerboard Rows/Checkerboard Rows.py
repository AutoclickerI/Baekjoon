for i in[0]*int(input()):
    d=[0]*9
    *l,=map(int,input().split())
    for j in l[2::2]:d[j]+=1
    print(max(d))