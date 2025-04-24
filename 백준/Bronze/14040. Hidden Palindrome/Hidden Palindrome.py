n=len(s:=input())
print(max(len((z:=s[i//n:i%n+1])*(z==z[::-1]))for i in range(n*n)))