for i in[*open(0)][1:]:
  r=''
  for i in map(int,i.split()):r+=chr(i).lower()if 64<i<91or 96<i<123else'-'
  print(r[1:]+r[0]+'ay')