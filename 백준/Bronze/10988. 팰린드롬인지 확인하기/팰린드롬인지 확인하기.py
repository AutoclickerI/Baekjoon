l=input()
b=1
for i in range(len(l)//2):
    if l[i]!=l[-i-1]:b=0
print(b)