d,_,l,_=map(str.split,open(0).read().split('#'))
for t in l:print([t,t[0]+'**'+t[3:]][len(t)>3and t[:4:3]in d])