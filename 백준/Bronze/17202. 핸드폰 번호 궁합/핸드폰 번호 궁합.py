x=[0]*16
x[::2]=input()
x[1::2]=input()
exec('x=[(int(i)+int(j))%10for i,j in zip(x,x[1:])];'*14)
print(*x,sep='')