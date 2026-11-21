l=[]
for i in[*open(0)][1].split():l+=[i:=int(i)]*(l[-1:]<[i])
print(len(l))
print(*l)