a,b=map(int,input().split())
s=0
for i in range(a+b):
    p,q=input().split()
    if p!=q:
        s+=1+(i<a)
        break
print(['Accepted','Why Wrong!!!','Wrong Answer'][s])