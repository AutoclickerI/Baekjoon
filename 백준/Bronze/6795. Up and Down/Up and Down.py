a,b,c,d,s=map(int,open(0))
print([(v:=sum((i%(a+b)<a)-(i%(c+d)<c)for i in range(s)))and'Byron'or'Tied','Nikky'][0<v])