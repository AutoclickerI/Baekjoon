s=input()
z=[]
for i in range(len(s)):
    z.append(s[i:])
z.sort()
print(*z,sep='\n')