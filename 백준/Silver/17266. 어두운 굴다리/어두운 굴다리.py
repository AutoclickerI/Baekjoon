N,M,*l=map(int,open(0).read().split())
l=0,*l,N
s,*dl,e=map(int.__sub__,l[1:],l)
print(max(s,e,*[i+1>>1for i in dl]))