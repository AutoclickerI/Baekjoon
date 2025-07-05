a,b,c,d,e,f=map(int,open(0).read().split())
n=(d-a)*360+(e-b)*30+f-c
k=n//720
print(n//360*(15+k)+k*~k,min(36,n//30),'%ddays'%n)