*l,=map(int,[*open(0)][1].split())
s={0}
for i in l:
 for j in[*s]:s|={j+i,j-i}
print(len({*range(sum(l)+1)}-s))