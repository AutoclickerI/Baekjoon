A,B,N=map(int,input().split())
s={A+B}
for _ in[0]*~-N:s={*[i+A for i in s],*[i+A+B for i in s]}
print(*sorted(s))