a,b,c=open(0)
ap=bp=cp=0
while ap<len(a)and bp<len(b)and cp<len(c):
    if a[ap]==b[bp]:
        v=a[ap]
        ap+=1
        bp+=1
    elif a[ap]==c[cp]:
        v=a[ap]
        ap+=1
        cp+=1
    else:
        v=b[bp]
        bp+=1
        cp+=1
    print(end=v)