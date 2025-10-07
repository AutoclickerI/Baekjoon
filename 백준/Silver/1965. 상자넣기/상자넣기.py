d=[0]*1001
for i in[*open(0)][1].split():i=int(i);d[i]=max(d[:i])+1
print(max(d))