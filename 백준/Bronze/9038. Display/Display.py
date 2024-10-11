for c in[0]*int(input()):
 w=int(input());a=input().split();r=1
 for b in a:
  if c+len(b)>w:r+=1;c=len(b)+1
  else:c+=len(b)+1
 print(r)