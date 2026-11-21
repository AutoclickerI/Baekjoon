_,p,q=map(str.split,open(0))
print(len(s:={*p}&{*q}),*sorted(s,key=int))