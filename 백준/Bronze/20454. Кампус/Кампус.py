N,K,X,Y=map(int,input().split())
input()
mod1=(N//K)*X+(N-N//K)*Y
mod2=X+~-K*Y
for i in map(int,input().split()):
    i-=1
    i=i%mod1
    f=i//mod2*K
    i%=mod2
    print(f+1+min(i//Y,K-1))