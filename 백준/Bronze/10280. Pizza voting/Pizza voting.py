n,p=map(int,input().split())
print('YNEOS'[1-(n//3<p<n-n//3+(n%3<2))::2])