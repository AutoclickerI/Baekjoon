for k in[0]*int(input()):
	N=int(input());A=*map(int,input().split()),;S=p=0
	while p<N:
		if p+A[k]<=N:p+=A[k];S+=p
		k=-~k%len(A)
	print(S)