c,n=map(int,input().split())
s='Sun Mon Tue Wed Thr Fri Sat\n'+4*~-c*' '
for i in range(c,n+c):s+=f'{i-c+1:3d} '+(i%7<1)*'\n'
print(s)