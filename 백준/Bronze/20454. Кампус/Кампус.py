N,K,X,Y=map(int,input().split())
input()
mod2=X+~-K*Y
for i in map(int,input().split()):
    i=(i-1)%((N//K)*X+(N-N//K)*Y)
    f=i//mod2*K
    i%=mod2
    print(f+1+min(i//Y,K-1))