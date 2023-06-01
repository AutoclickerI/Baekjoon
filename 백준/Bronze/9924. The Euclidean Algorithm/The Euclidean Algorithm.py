p,q=map(int,input().split());n=0
while k:=p-q:p,q=abs(k),min(p,q);n+=1
print(n)