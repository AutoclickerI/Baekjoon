N,M=map(int,input().split())
f=(2<N)*M
print(+(N<2)or max(min(4,(f-~M)//2),f-2))