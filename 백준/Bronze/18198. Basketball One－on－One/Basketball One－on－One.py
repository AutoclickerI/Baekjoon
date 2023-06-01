a={'A':0,'B':0}
l=input()
for i in range(len(l)//2):
    a[l[2*i]]+=int(l[2*i+1])
print('A'if a['A']>a['B']else'B')