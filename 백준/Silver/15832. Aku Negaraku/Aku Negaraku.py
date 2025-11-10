while 1:
 N,M=map(int,input().split())
 if N+M<1:break
 j=0
 for i in range(2,N+1):j=(j+M)%i
 print(j+1)