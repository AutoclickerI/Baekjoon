l=[]
for i in[0]*int(input()):
    p,q=map(int,input().split())
    if p<=q:l+=[q]
try:print(min(l))
except:print(-1)