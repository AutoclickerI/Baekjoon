l=[0,1,2,3]
c=[0]*4
for i in[*open(0)][1:]:a,b,g=map(int,i.split());l[a],l[b]=l[b],l[a];c[l[g]]+=1
print(max(c))