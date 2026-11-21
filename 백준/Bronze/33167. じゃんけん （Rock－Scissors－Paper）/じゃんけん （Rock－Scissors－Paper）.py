_,a,b=open(0)
p=P=0
for i,j in zip(a,b):
    if i+j in'SP PR RS':p+=1
    if i+j in'PS RP SR':P+=1
print(p,P)