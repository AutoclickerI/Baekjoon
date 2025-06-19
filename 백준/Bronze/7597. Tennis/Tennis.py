while'#'<(s:=input()):
 x=y=0;v=['A',0,'B',0]
 for i in s:
  x+=i<'B';y+='A'<i
  if max(x,y)>3>1<abs(x-y):v[1+(x<y)*2]+=1;x=y=0
 print(*v)