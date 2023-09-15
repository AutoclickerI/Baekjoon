from itertools import*
for i in[0]*int(input()):
    l=[[*map(int,input().split())]for _ in[0]*int(input())]
    f=lambda a:(a[0][0]-a[1][0])**2+(a[0][1]-a[1][1])**2
    s=sorted(combinations(l,2),key=f)
    m=f(s[0])
    ansli=[]
    while i<len(s) and f(s[i])==m:
        ansli+=' '.join(str(i)for i in sum(sorted(s[i]),[])),
        i+=1
    print(min(ansli))