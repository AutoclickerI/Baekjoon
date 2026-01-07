N,*l=map(int,open(0).read().split())
print(max(map(sum,zip(l:=N%2*[0]+sorted(l),l[::-1]))))