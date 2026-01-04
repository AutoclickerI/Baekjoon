v=0
r=1
for i in range(int(input())):v,r=r,i*(v+r)%10**9
print(r)