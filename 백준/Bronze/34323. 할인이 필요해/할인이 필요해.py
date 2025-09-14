N,M,S=map(int,input().split())
print(min(M*S,~M*S*(N-100)//100))