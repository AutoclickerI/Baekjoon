l=[0,0,0]
for i in[*open(0)][1:]:l[eval(i.replace(*' -'))%3]+=1
print(max(l[1:]))