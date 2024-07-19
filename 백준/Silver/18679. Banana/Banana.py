I,d=input,{}
for x,y in eval('I().split(" = "),'*int(I())):d[x]=y
exec('I();print(*map(d.get,I().split()));'*int(I()))