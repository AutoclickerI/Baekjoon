x=[0]*16
x[::2]=input()
x[1::2]=input()
while len(x)-2:x=[(int(i)+int(j))%10for i,j in zip(x,x[1:])]
print(*x,sep='')