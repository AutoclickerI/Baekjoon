N,*l=map(int,open(0))
l+=l
print(min(sum(x*y for x,y in enumerate(l[i:i+N-1],1))for i in range(N)))