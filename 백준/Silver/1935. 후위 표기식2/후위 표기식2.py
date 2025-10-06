n,x,*l=open(0)
s=[]
for e in x[:-1]:s=s+[int(l[ord(e)-65])]if'@'<e<'['else s[:-2]+[eval(f's[-2]{e}s[-1]')]
print(f'{s[0]:.2f}')