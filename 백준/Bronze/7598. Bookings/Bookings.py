while'$'<(s:=input()):
 a,b=s.split();b=int(b)
 while(s:=input())<'X':c,d=s.split();d=int(d);b+=d*[-(d<=b),b+d<69][c<'C']
 print(a,b)