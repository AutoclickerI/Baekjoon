(_,C),*l=[map(int,i.split())for i in open(0)]
print(min(p+d+C*v for p,d,v in l))