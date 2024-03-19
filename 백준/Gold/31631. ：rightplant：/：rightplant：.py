l=[]
for i in range(n:=int(input())):l.insert(len(l)//2+(i%4==3),n-i)
print(*l)