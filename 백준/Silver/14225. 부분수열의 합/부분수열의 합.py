N,*l=map(int,open(0).read().split())
s=set()
for i in range(2**N):
    v=j=0
    while i:
        v+=i%2*l[j]
        j+=1
        i//=2
    s|={v}
i=0
while i in s:i+=1
print(i)