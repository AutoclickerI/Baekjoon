a,b=map(int,open(0),[2,2])
v=10**5
for i in a&b,a|b,a^b,2**v+~a,2**v+~b:print(f'{i:b}'.zfill(v))