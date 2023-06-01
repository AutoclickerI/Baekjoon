M,S,G=map(float,input().split())
A,B=map(float,input().split())
L,R=map(float,input().split())
print(['latmask','friskus'][M/G+L/A<M/S+R/B])