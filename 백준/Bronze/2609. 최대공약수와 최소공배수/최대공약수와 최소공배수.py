a=list(map(int, input().split()));a.sort();b=a[-1]
while a[0]%b+a[1]%b!=0:b-=1
print(b);x,y=a
while x!=y:
    if x<y:x+=a[0]
    else:y+=a[1]
print(x)
    