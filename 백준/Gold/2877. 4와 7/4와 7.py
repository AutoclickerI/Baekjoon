l=[2<<i for i in range(40)]
sl=[0]
for i in l:sl+=sl[-1]+i,

N=int(input())
s=''
i=0
while sl[i]<N:i+=1
i-=1
N-=sl[i]+1

while i:
    if l[i-1]<=N:
        s+='7'
        N-=l[i-1]
    else:
        s+='4'
    i-=1
print(s+'47'[N])