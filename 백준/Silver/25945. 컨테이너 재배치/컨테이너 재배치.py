S=sum
n,*l=map(int,open(0).read().split())
a=0-S(l)//-n
print(max(S(a+~x for x in l if x<a-1),S(x-a for x in l if x>a)))