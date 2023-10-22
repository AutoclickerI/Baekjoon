H,P=map(int,input().split())
a,b=500000,6000000
d=0
t=1000
while a<b:
    d+=1
    a+=60*H*P
    b+=11*H*P
    t-=H
    if t<0:
        a+=500000
        t+=1000
print(d)