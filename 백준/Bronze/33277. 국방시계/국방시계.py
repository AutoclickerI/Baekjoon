N,M=map(int,input().split())
print('%02d:%02d'%divmod(1440*M//N,60))