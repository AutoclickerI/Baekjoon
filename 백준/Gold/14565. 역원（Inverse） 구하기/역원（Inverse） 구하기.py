p,q=map(int,input().split())
try:x=pow(q,-1,p)
except:x=-1
print(p-q,x)