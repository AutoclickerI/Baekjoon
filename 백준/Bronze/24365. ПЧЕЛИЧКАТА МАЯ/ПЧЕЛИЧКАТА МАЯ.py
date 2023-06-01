a,b,c=map(int,input().split())
d=sum([a,b,c])//3
num=c-d
b,c=b+(c-d),d
print(num+b-d)