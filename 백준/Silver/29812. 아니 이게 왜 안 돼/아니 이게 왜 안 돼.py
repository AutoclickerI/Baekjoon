n=int(input())
s=input()
D,M=map(int,input().split())
c=0
t=[]
d={}
for i in s:
    if i in'HYU':
        d[i]=d.get(i,0)+1
        t+=c,
        c=0
    else:
        c+=1
t+=c,
print(sum(min(D*i,M+D)for i in t)or'Nalmeok')
print(min(d.get('H',0),d.get('Y',0),d.get('U',0))or'I love HanYang University')