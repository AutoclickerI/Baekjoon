v=7368792
*p,=range(v)
for i in range(2,v):
    if p[i]:
        p[2*i::i]=[0]*len(range(2*i,v,i))
p=[i for i in p if i]
print(p[int(input())])