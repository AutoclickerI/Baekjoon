n=int(input())
s=input()
def diff(s1,s2):
    return sum(i!=j for i,j in zip(s1,s2))
for i in range(n):
    if diff(s,s[-1-i:])==1:print('YES');exit()
print('NO')