for i in range(int(input())):
    n,m=map(int,input().split())
    l=[[*map(int,input().split())]for _ in[0]*n]
    Mx=My=-1e99
    mx=my=1e99
    for j in map(int,input().split()):
        p,q=l[j-1]
        Mx=max(Mx,p)
        mx=min(mx,p)
        My=max(My,q)
        my=min(my,q)
    cnt=0
    for p,q in l:
        cnt+=mx<=p<=Mx and my<=q<=My
    print(f'Data Set {i+1}:\n{cnt}\n')