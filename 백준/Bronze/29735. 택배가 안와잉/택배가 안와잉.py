h,m,H,M,N,T=map(int,open(0).read().replace(*': ').split())
t=((H-h)*60+M+~m)//T
v=m-~(N%t)*T
print(N//t,f'{h+v//60:02}:{v%60:02}')