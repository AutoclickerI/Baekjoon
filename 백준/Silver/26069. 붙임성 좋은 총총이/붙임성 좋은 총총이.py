dance={'ChongChong'}
for _ in[0]*int(input()):
    p,q=input().split()
    if p in dance:
        dance.add(q)
    if q in dance:
        dance.add(p)
print(len(dance))