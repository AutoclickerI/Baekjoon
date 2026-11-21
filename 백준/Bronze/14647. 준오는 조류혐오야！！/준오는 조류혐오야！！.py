_,*l=open(0)
print(sum(map(f:=str.count,l,n:='9'*9999))-max(map(f,[*l,*map(''.join,zip(*map(str.split,l)))],n)))