N,*l=open(0)
Z=ord(N[-2])%4
print(len({*l})//Z) 