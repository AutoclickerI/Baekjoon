(_,H),*l=[map(int,i.split())for i in open(0)]
f=a=0
for i in l:t=sorted(i);f|=H<t[0];a+=t[H<t[1]]
print(f*'impossible'or a)