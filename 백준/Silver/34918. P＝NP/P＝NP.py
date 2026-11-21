def f(s):
 p=n=0
 for c in s:f=c<'P';n=n*f+f;p+=1-f;
 return p,n
for i in[*open(0)][1:]:s,e=i.split();print('YNEOS'[f(s)!=f(e)::2])