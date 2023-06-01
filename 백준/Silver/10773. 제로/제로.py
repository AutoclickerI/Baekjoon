a=[]
for i in range(int(input())):
 n=int(input())
 if n==0:del a[-1]
 else:a.append(n)
print(sum(a))