for*s,_ in[*open(0)][1:]:
  o=0
  for i in range(len(s)):
    if's'==s[i]!=i!=0:
      try:
        if'h'!=s[i+1]:s[i]='th'
      except:s[i]='th'
    elif i<1:
      if'e'==s[i]:s[i]='ae'
      if'E'==s[i]:s[i]='Ae'
  for i in range(len(s)):
    if s[i]in'Oo':
      o+=1
      if o==2:s[i]='u'
    else:o=0
  print(*s,sep='')