(_,H),*l=[map(int,i.split())for i in open(0)]
f=a=0
for l,w,h in map(sorted,l):f|=H<l;a+=[l,w][H<w]
print(f*'impossible'or a)