l=[[*map(int,i.split())]for i in open(0)][1:]
s=[l[0]]
for i in l[1:]:
    if i[0]<=s[-1][1]:
        s[-1][1]=max(s[-1][1],i[1])
    else:
        s+=i,
print(sum(j-i for i,j in s))