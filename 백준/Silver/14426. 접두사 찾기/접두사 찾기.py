N,M=map(int,input().split())
s=set()
for _ in[0]*N:
    v=input()
    for i in range(len(v)):
        s.add(v[:i+1])
print(sum(input()in s for _ in[0]*M))