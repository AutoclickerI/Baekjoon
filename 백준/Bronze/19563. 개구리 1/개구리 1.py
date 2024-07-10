a,b,c=map(int,input().split())
print('YNEOS'[c<abs(a)+abs(b)or a+b-c&1::2])