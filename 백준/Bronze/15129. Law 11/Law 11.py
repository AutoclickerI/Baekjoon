b,*l=([*map(int,i.split())][0]for i in open(0))
print(+(max(l[:11])>max(0,b,sorted(l[11:])[-2])))