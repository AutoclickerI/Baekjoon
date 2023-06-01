s='I'+'OI'*int(input())
input()
l=input()
i=0
a=-1
L=0
while L+1:
    L=l[i:].find(s)
    i=i+L+1
    a+=1
print(a)