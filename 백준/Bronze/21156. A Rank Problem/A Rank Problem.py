n,*a=map(str.split,open(0))
t=[f'T{i+1}'for i in range(int(n[0]))]
for p,q in a:
 x,y=map(t.index,(p,q))
 if x>y:t.pop(y);t.insert(x,q)
print(*t)