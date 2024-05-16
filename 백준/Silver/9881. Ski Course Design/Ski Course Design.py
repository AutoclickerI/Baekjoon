_,*l=map(int,open(0))
print(min(sum(max(i-c,c-i-17,0)**2for c in l)for i in range(84)))