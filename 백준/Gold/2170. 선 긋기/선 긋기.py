[N],*z=[[*map(int,i.split())]for i in open(0)]
z.sort()

l=[z[0]]

for s,e in z[1:]:
    if s<=l[-1][1]:
        l[-1][1]=max(l[-1][1],e)
    else:
        l+=[s,e],

print(sum(j-i for i,j in l))