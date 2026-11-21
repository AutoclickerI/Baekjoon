S=sum
n,*l=map(int,open(0).read().split())
a=0-S(l)//-n
print(max(S(a-x-1for x in l if~-a>x),S(x-a for x in l if x>a)))