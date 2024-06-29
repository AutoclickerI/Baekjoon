N=int(input())%100
c=10
while N-c>=0:N-=c;c+=10
print(0-min(N,c-N)//-5)