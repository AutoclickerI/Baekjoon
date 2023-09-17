*l,=zip(input(),input())
s=sum(l,())
for _ in[0]*int(input()):
    p=1
    for i in input():
        if i.isupper()and i not in s:
            p=0
        if i.islower()and(i,i)not in l:
            p=0
    print(['Not their baby!','Possible baby.'][p])