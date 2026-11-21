*p,=range(999)
for i in range(2,999):
 if p[i]:p[2*i::i]=[0]*(998//i-1)
p={*p}-{1,0}
for i in[*open(0)][1:]:n=int(i)-3;print(*[sorted([3,i,n-i])for i in p if n-i in p][0])