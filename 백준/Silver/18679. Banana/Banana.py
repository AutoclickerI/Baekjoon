I=input
d={x:y for x,_,y in eval('I().split(),'*int(I()))}
exec('I();print(*map(d.get,I().split()));'*int(I()))