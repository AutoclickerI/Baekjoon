n,d=input().split()
print([d.ljust(n:=int(n),'0'),'No solution'][n<len(d)])