A,B,C,I,J,K=map(int,open(0).read().split())
m=min(A/I,B/J,C/K)
print(A-m*I,B-m*J,C-m*K)