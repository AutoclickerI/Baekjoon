N=int(input())
s=input()
c=[float('inf')]*N
c[0]=0
for i in range(1,N):
    for j in range(i):
        if s[j]+s[i]in'BO OJ JB':
            c[i]=min(c[i],c[j]+(j-i)**2)
print(-(c[-1]==float('inf'))or c[-1])