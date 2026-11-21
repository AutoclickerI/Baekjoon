b=[0,1,0,0]
for i in input():
    if i=='A':
        b[1:3]=b[2:0:-1]
    if i=='B':
        b[2:4]=b[3:1:-1]
    if i=='C':
        b[1::2]=b[3::-2]
print(b.index(1))