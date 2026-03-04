N=int(input())
s=input()
l=[]
for i in range(N):
    if s[i]=='H'and s[max(0,i-2):i+2]=='SSHS':
        l+=1,
    elif s[i]=='H'and s[max(0,i-2):i+2]=='GSHS':
        l+=-1,
    else:
        l+=0,
m=v=0
for i in l:
    v=max(v,0)+i
    m=max(m,v)
print(m)