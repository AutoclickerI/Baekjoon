n,*l=open(0)
v,x=0,[[0]*3,[0]*3]
for s in l:
 b='N'<s[0];v+=b
 for i in 0,1,2:x[b][i]+='N'<s[i+1]
for i,j in zip(*x):print(['Not Effective',x:=(1-j*(int(n)/v-1)/i)*100][x>0])