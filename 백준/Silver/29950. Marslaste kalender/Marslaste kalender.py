A,B=map(int,input().split())
s=0
M=m=1
while m<=B:s-=m*~m;B-=m;m+=1
while M<A:s+=M*~M;A-=M;M+=1
print(s-A*~-A-B*~B>>1)