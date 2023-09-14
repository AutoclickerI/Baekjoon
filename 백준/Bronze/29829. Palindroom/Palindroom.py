*l,=map(int,input().split())
if sum(i>j for i,j in zip(l,l[::-1]))>1:print('EI')
else:print('JAH',*l[:len(l)//2]+l[~-len(l)//2::-1])