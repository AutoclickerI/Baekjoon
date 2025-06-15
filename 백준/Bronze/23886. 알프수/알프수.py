s=input()
g=[int(j)-int(i)for i,j in zip(s,s[1:])]
l=[g[0]]
for i in g:l+=[i]*(i!=l[-1])
print('NON ALPSOO'[4*all(i*j<0for i,j in zip(l,l[1:]))*(l[-1]<0<l[0]):])