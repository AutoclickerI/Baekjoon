a,b,c=map(int,input().split())
s=sum(l:=sorted(map(int,input().split())))
print(sum(l[-b-c:])*100/s)