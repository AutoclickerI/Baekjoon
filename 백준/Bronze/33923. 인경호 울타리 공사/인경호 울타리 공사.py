N,M=sorted(map(int,input().split()))
f=M-N<1
print((N-1-f)**2+f)