a,b=map(int,input().split())
for i in range(a,b+1):print(['Palindrome!',p:=str(i)][p!=p[::-1]])