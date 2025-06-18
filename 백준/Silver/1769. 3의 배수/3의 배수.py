s=input()
i=0
while 1<len(s):
    i+=1
    s=str(sum(map(int,s)))
print(i)
if s in'369':print('YES')
else:print('NO')