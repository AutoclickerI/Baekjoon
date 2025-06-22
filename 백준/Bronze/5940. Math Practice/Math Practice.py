a,b=input().split()
f=0
for i in range(62,int(a),-1):f=[f,i][str(2**i)[0]==b]
print(f)