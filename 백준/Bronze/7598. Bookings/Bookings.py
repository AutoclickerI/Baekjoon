while'$'<(s:=input()):
 a,b=s.split();b=int(b)
 while(s:=input())<'X':d=int(s[1:]);b+=d*[-(d<=b),b+d<69][s<'C']
 print(a,b)