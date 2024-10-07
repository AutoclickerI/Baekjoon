s=input()
n=int(input())
a='zz'
for i in range(len(s)-1):p=s[i:i+2];a=min(a,p,p[::-1])
print(n//2*a+n%2*a[0])