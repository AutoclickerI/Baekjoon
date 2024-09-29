n=int(input())
m=n//2+1
for i in range(n):print(m:=(n|1)-m+~i%2)