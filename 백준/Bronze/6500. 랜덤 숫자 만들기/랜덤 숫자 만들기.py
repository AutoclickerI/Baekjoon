while n:=int(input()):
 s={n}
 while{n:=n*n//100%1e4}-s:s|={n}
 print(len(s))