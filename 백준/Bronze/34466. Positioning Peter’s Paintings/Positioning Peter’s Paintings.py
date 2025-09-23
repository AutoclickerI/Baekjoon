A,B,X,Y=map(int,input().split())
print(min(max(A,X)+B+Y,max(B,Y)+A+X)*2)