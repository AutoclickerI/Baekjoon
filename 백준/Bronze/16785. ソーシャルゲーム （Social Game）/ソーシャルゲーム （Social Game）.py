a,b,c=map(int,input().split())
C=0
while a*C+C//7*b<c:C+=1
print(C)