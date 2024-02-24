*l,=map(int,[*open(0)][1].split())
s={0}
for i in l:s|={*sum([[j+i,j-i]for j in s],[])}
print(len({*range(sum(l)+1)}-s))