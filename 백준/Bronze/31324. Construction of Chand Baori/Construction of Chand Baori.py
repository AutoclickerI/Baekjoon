N,M=map(int,input().split())
s=1
while N:s*=N*2;N-=1
print(['Harshat Mata','Nope'][M>s])