_,p,q=map(str.split,open(0))
print(*sorted({*p}&{*q},key=int))