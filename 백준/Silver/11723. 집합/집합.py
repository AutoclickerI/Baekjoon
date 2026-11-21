import sys
d=[0]*21
for _ in range(int(input())):
    l=sys.stdin.readline().split()
    if l[0]=='add':d[int(l[1])]=1
    elif l[0]=='check':print(d[int(l[1])])
    elif l[0]=='remove':d[int(l[1])]=0
    elif l[0]=='toggle':d[int(l[1])]^=1
    elif l[0]=='all':d=[1]*21
    else:d=[0]*21