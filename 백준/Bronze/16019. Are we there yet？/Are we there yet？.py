a=[i:=0]
for j in input().split():i+=int(j);a+=i,
for i in a:
 for j in a:print(abs(j-i))