I=input
exec('print(min((j/i,j)for i,j in eval("[*map(int,I().split())],"*int(I())))[1]);'*int(I()))