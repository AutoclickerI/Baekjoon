for n in[*map(int,open(0))][1:]:
 l=[]
 while n:l=[n%3]+l;n//=3
 print(*l)