N,M=map(int,input().split())
print('Can'+"'t"*(N%-~M==1),'win')