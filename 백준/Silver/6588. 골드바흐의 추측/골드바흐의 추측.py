*l,=range(6**8)

for i in range(2,6**8):
    if l[i]:l[2*i::i]=[0]*len(l[2*i::i])

l=[i for i in l if 2<i]
sl={*l}

while n:=int(input()):
    for i in l:
        if n-i in sl:print(n,'=',i,'+',n-i);break