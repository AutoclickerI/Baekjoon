*l,=map(int,[*open(0)][1].split())
d=[]
for i in l:d+=max(j+abs(i-k)for j,k in zip([0]+d,l)),
print(d[-1])