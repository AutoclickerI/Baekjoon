N=int(input())
i=0
while len(str(i))<=N:N-=len(str(i));i+=1
print(str(i)[N])