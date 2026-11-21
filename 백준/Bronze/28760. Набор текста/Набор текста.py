z=int(input())
p=0
for s in input():
  if s in'!?$()'or'@'<s<'[':z+=p<1;p=1
  else:p=p*(' '==s)
print(z)