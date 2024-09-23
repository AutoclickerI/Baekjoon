C=input()
for _ in[0]*int(input()):
 l=[[],[]]
 for i,c in enumerate(C[::-1]):l[i%2]+=c
 C=l[1]+l[0]
print(*C,sep='')