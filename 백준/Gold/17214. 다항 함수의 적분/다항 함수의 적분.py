n=input().replace('-','+-').split('+')
if n[0]=='':del n[0]
if len(n)==2:
 N=int(n[0][:-1])//2
 N=N if N!=1 else''
 N=N if N!=-1 else'-'
 N1=int(n[1])
 N1=N1 if N1!=1 else''
 N1=N1 if N1!=-1 else'-'
 if int(n[1])>0:print(N,'xx+',N1,'x+W',sep='')
 else:print(N,'xx',N1,'x+W',sep='')
else:
 try:
  N1=int(n[0])
  N1=N1 if N1!=1 else''
  N1=N1 if N1!=-1 else'-'
  if int(n[0]):print(N1,'x+W',sep='')
  else:print('W')
 except:
  N=int(n[0][:-1])//2
  N=N if N!=1 else''
  N=N if N!=-1 else'-'
  print(N,'xx+W',sep='')