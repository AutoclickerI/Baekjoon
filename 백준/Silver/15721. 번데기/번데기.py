N,M,T=map(int,open(i:=0))
j=3
while~-M>j:j+=1;i+=2*j;M-=j
i+=2//M*(~-M*2+T)or~-j*T-~M
print(i%N)