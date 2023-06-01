p,q=map(int,input().split())
l=[input()for _ in[0]*p]
d=[input()for _ in[0]*q]
dic={}
s=1
for i in l:
    dic[i]=s
    dic[str(s)]=i
    s+=1
for i in d:
    print(dic[i])