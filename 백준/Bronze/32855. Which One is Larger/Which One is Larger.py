o,p=l=[*open(0)]
x,y=map(eval,l)
a,b=map(lambda i:[*map(int,i.split('.'))],l)
print(o*(x>y)*(a>b)or p*(x<y)*(a<b)or-1)