n=int(input())
l=~n%2*[1]
for i in range(n-~n%2):
 if i%4<2:l+=i+2-n%2,
 else:l=[i+2-n%2]+l
print(*min(l,l[::-1]))