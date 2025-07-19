i=0
while'a'<(s:=input()[::2]):
 print('Case',i:=i+1)
 for _ in[0]*int(input()):
  v=input()
  for c in s+s.upper():v=v.replace(c,'_')
  print(v)
 print()