a,b=open(0)
if len(b)>len(a)or a==b:
    exit(print('Bad luck'))
if int(a)>int(b):
    print(0)
else:
    print(1)
    for i in range(len(a)):
        if a[i]<b[i]:
            exit(print(i+1))