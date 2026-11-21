n=int(input())
print(max(i+j-n for i,j in zip(range(n),map(int,input().split()))))