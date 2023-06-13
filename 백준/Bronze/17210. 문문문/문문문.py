p,q=map(int,open(0))
if p>5:print('Love is open door')
else:
    for _ in range(p-1):
        q^=1
        print(q)