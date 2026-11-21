A,B,K,X=map(int,open(0).read().split())
print(len({*range(A,B+1)}&{*range(K-X,K+X+1)})or'IMPOSSIBLE')