input()
d={}
for idx,i in enumerate(input().split()):
    d[i]=d.get(i,0)+1
    if d[i]==5:exit(print(idx+1))
print(0)