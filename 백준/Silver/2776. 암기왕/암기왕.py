_,*l=map(str.split,open(0))
while l:_,d,_,s,*l=l;d={*d};print(*[+(i in d)for i in s])