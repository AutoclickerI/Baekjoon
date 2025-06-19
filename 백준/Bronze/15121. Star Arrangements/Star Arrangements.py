n=int(s:=input())
print(s+':',*[f'{i},{j}'for i in range(2,n)for j in[i-1,i]if n%(i+j)%i<1])