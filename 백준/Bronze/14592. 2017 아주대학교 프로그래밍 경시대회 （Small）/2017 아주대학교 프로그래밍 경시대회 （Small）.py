l=[]
for i in range(int(input())):
    *p,=map(int,input().split())
    p[0]*=-1
    l+=[p+[i+1]]
print(sorted(l)[0][3])