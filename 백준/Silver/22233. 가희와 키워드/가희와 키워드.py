N,_,*l=open(0).read().split()
N=int(N)
s={*l[:N]}
for i in l[N:]:s-={*i.split(',')};print(len(s))