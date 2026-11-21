N,*l=map(eval,open(0).read().split())
print(sum(max(int(i*k+.01)-j,i-int(j*k+.01))for i,j,k in zip(l,l[N:],l[2*N:])))