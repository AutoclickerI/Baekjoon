l=sorted(range(*eval(input().replace(' ',',1+'))),key=lambda n:[*map('549176320'.find,str(n))])
while l:print(*l[:10]);l=l[10:]