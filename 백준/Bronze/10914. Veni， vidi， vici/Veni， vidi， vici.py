N,A=open(0,'rb')
for k in A.split():print(''.join(chr((i+j+14-int(N))%26+97)for i,j in zip(*[iter(k)]*2)))