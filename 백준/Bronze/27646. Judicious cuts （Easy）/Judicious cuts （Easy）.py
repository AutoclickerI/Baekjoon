for i in open(0).read().split()[1:]:
 print(i:=int(i)-1)
 for _ in[n:=0]*i:print(-1,n:=n-1)