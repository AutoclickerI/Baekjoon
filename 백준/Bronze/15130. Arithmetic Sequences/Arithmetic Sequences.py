*s,=map(int,input().split())
R=range(10)
a,b=[i for i in R if s[i]]
d=(z:=s[b]-s[a])//(b-a)
print(*z%(b-a)and[-1]or[s[a]+d*(i-a)for i in R])