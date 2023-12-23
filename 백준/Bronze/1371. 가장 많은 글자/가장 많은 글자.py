f=open(0).read().count
m=max(map(lambda i:f(chr(i)),range(97,123)))
for i in range(97,123):
    if f(chr(i))==m:print(end=chr(i))