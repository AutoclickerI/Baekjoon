d,m,w,i,j,k=map(int,open(0).read().split())
print(chr(97+(i+j*d+k*d*m-1-d-d*m)%w))