*ret,N=map(int,input().split())

s=0
if 0<N and ret[0]<0:
    s=1
    ret[0]*=-1

i=0
while i<len(ret):
    over=ret[i]//abs(N)
    ret[i]%=abs(N)
    if over:
        if i==len(ret)-1:
            ret+=0,
        if 0<N:
            ret[i+1]+=over
        else:
            ret[i+1]-=over
    i+=1

print('-'*s,*ret[::-1],sep='')