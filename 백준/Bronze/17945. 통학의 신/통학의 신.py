A,B=map(int,input().split())
print(*sorted({int(-A+(A*A-B)**.5),int(-A-(A*A-B)**.5)}))