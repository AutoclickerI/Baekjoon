n,*l=map(int,open(0).read().split())
print('yneos'[any(l[2*i]>l[2*i+2]or l[2*i+1]>l[2*i+3]for i in range(n-1))::2])