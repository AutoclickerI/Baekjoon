for T in range(int(input())):
    v={0}
    s,e,t=input().split()
    l=[(0,0)]
    f=1
    for i,j in l:
        n=i+j
        if n==len(t):
            f=0
            break
        nv=[]
        if t[n]==s[i:i+1]:
            nv+=(i+1,j),
        if t[n]==e[j:j+1]:
            nv+=(i,j+1),
        for i in nv:
            if i not in v:
                v.add(i)
                l+=i,
    print(f'Data set {T+1}:','yneos'[f::2])