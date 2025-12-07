U,O,S=map(int,input().split())
k=max(U-S,0)//3
print(min(U-2*k,O,S+k))