a=input().split()
i=1
while sum(i%int(w)<1for w in a)<3:i+=1
print(i)