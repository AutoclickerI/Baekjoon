_,*l=[sorted(s.split()[1:])[::-1]for s in open(0)]
while l:a,b,*l=l;print('DAB'[(a>b)-(a<b)])