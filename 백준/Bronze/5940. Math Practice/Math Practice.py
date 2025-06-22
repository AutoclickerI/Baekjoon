a,b=input().split()
f=0
for i in range(62,int(a),-1):
 if str(2**i)[0]==b:f=i
print(f)