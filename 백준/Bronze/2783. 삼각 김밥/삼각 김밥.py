a,b=map(int,input().split())
l=[a*1e3/b]
for i in[0]*int(input()):a,b=map(int,input().split());l+=[a*1e3/b]
print(min(l))