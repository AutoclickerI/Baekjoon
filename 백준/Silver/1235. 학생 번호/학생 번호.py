_,*l=open(k:=0)
while len({i[~k:]for i in l})<len(l):k+=1
print(k)