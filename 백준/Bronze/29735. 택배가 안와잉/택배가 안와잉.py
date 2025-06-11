h,m,H,M,N,T=map(int,open(0).read().replace(*': ').split())
t=(H*60+M-h*60-m-1)//T
z=N//t
N%=t
N+=1
v=h*60+m+N*T
print(z,f'{v//60:02}:{v%60:02}')