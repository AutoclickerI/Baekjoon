N=int(input())
s=[]
while N:
    v=N%4
    if v==0:
        s+='00'
    if v==1:
        s+='10'
        N-=1
    if v==2:
        s+='01'
        N+=2
    if v==3:
        s+='11'
        N+=1
    N//=4
print(''.join(s[::-1]).lstrip('0')or'0')