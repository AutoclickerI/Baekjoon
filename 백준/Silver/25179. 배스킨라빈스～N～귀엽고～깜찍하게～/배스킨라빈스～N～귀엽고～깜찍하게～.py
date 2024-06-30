N,M=map(int,input().split())
print('Can'+"'t"*(1-M-N%~M),'win')