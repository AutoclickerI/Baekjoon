a1,a2,a3,b1,b2,b3,l=map(int,input().split())
m=9**9
for i in range(b1+1):
    for j in range(b2+1):
        for k in range(b3+1):
            if a1*i+a2*j+a3*k>=l:
                m=min(i+j+k,m)
if m!=9**9:print(m)
else:print(0)