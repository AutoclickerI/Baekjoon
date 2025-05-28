N,*l=int(input()),
exec('l=sorted(l+input().split(),key=int)[-N:];'*N)
print(l[0])