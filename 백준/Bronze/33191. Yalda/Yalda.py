v=0
a,b,c,d=map(int,open(0))
if a>=b:
    v=1
elif a>=c:
    v=2
elif a>=d:
    v=3
print(['Nothing','Watermelon','Pomegranates','Nuts'][v])