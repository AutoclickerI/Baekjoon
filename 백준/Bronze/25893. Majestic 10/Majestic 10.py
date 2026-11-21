_,*q=open(0)
for i in q:
    l=sum(map(lambda x:int(x)>9,i.split()))
    L=['zilch','double','triple']
    print(i+(L[0]if l==0 else L[1]if l==1 else L[1]+'-'+L[1]if l==2 else L[2]+'-'+L[1])+'\n')