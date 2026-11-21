l=[]
for i in[0]*int(input()):
    p,q,r,s=input().split()
    l+=[[int(s),int(r),int(q),p]]
l.sort()
print(l[-1][3],l[0][3])