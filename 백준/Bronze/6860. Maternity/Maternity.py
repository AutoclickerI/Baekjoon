a,b,_,*L=open(0)
*l,=zip(a,b)
for j in L:
    p=1
    for i in j:
        if i.isupper()and i not in sum(l,()):
            p=0
        if i.islower()and(i,i)not in l:
            p=0
    print(['Not their baby!','Possible baby.'][p])