w,a,p=0,'',' '
for c in input()+'a':
 match w+(v:=c in'aeiou'):
  case 2:continue
  case 0 if c==p:continue
  case 0 if p!=' ':a+='a'
 a,p,w=a+{'r':'l','s':'k'}.get(c,c),c,v
print(a)