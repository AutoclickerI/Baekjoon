input()
r,c,x,y=map(int,input().split())
a=abs(r-x)
b=abs(c-y)
l=a//2
print([l+max(0,(b-l)//2),-1][a%2 or l%2^b%2])