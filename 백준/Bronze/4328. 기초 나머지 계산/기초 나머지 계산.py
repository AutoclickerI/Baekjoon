while'0'<(s:=input()):
 b,p,m=s.split();a='';n=int(p,b:=int(b))%int(m,b)
 while n:a=str(n%b)+a;n//=b
 print(a or 0)