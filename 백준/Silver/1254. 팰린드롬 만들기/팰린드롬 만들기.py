def pal(s):
    return all(i==j or'*'in[i,j]for i,j in zip(s,s[::-1]))
s=input()
while pal(s)<1:s+='*'
print(len(s))