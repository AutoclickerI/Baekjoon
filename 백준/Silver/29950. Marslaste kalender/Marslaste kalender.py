A,B=map(int,input().split())
s=m=1
while(x:=m<=B)|(y:=m<A):s-=m*~m*(x-y);A-=m*y;B-=m*x;m+=1
print(s-A*~-A-B*~B>>1)