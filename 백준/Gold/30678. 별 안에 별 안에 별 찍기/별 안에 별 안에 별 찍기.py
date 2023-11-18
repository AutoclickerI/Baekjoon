star=['*']
for i in range(int(input())):
    tmp=[' '*2*5**i+s+' '*2*5**i for s in star]*2
    tmp+=[s*5 for s in star]
    tmp+=[' '*5**i+s*3+' '*5**i for s in star]
    tmp+=[' '*5**i+s+' '*5**i+s+' '*5**i for s in star]
    star=tmp
for i in star:
    print(i)