N,s,P,*l=map(int,open(0).read().split())
l+=s,
l.sort()
print(-(s in l[:-P])or-~l[::-1].index(s))