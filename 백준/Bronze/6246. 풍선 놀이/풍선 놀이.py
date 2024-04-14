(N,_,*a),*l=[map(int,i.split())for i in open(0)]
for i,j in l:a+=range(i,N+1,j)
print(N-len({*a}))