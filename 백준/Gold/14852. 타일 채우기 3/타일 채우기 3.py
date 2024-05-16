a,b,c=1,2,7
for _ in[0]*int(input()):a,b,c=b,c,(3*c+b-a)%(10**9+7)
print(a)