f=input().replace
for i in range(10):s=f('*',str(i));sum(map(int,s+s[1::2]*2))%10<1<exit(print(i))