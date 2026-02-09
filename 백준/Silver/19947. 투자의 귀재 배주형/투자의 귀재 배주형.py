*H,Y=map(int,input().split())
l=[0]*4+H
exec('l+=max(l[-1]*7,l[-3]*8,l[-5]*9)*3//20,;'*Y)
print(l[-1])