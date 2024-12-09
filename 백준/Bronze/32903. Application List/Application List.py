l=['.']*26
for c,*_ in[*open(0)][1:]:
    l[ord(c)-97]=c

for i in range(6):
    for j in l[6*i:6*i+6]:
        print(end=j)
    print()