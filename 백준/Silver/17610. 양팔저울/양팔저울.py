input()
*l,=map(int,input().split())
s={0}
for i in l:s|={j+i for j in s}|{j-i for j in s}
print(len({*range(1,sum(l)+1)}-s))