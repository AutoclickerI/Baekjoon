_,(y,x),*l=[map(int,i.split())for i in open(0)]
a=0
for i,j in l:a+=(sum,max)[0<(y-i)*(x-j)]([abs(y-i),abs(x-j)]);y,x=i,j
print(a)