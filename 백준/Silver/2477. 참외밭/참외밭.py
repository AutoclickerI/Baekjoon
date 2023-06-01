n=int(input())
l=[]
x=y=0
for i in[0]*6:
    a,b=map(int,input().split())
    if a==1:
        x+=b
    elif a==2:
        x-=b
    elif a==3:
        y-=b
    else:
        y+=b
    l+=[[x,y]]
l+=[l[0]]
s=0
for i in range(6):
   s+=l[i][0]*l[i+1][1]-l[i+1][0]*l[i][1]
print(abs(s)//2*n)