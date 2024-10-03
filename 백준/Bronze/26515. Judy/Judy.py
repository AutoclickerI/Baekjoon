for i in[*open(0)][1:]:
  r=''
  for i in map(int,i.split()):r+=chr(i).lower()if 65<=i<=90 or 97<=i<=122else'-'
  print(r[1:]+r[0]+'ay')