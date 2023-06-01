N,K=map(int,input().split())
print('YNEOS'[N>sum((int(i)+1)//2for i in input().split())::2])