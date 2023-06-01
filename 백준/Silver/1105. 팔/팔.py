L,R=input().split()
a=0
for i,j in zip(L,R):
 if i!=j:break
 a+=i=='8'
print(a*(len(L)==len(R)))