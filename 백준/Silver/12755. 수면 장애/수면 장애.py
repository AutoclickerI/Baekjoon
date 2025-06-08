N=int(input())-1
i=1
while len(str(i))<=N:
    N-=len(str(i))
    i+=1
print(str(i)[N])