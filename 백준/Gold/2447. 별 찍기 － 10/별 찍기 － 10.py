n,s,i=int(input()),'*',1
while i<n:k=[c*3for c in s];s=k+[c+' '*i+c for c in s]+k;i*=3
print(' '.join(s))