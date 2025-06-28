v=[7,5,5,4,5,4]
d=[7]*4+[*v,7,7,4,5,*v,5]+[7]*4
l=[]
input()
for i in input():l+=d[ord(i)-65::5],
for i in zip(*l):print(''.join(f'{j:03b}'.translate(str.maketrans('10','*.'))for j in i))