s1,s2=open(0)
l=[[0]*len(s2)for _ in[0]*len(s1)]
for i in range(1,len(s1)):
    for j in range(1,len(s2)):
        l[i][j]=-~l[i-1][j-1]*(s1[i-1]==s2[j-1])
print(max(max(i)for i in l))