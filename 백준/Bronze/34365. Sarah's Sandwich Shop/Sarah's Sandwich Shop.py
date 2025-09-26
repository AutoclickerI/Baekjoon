w='22233344455566677778889999'
for i in[*open(0)][1:]:
    for c in i.lower()[:-1]:
        print(end=w[ord(c)-97])
    print()