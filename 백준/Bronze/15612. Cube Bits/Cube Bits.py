for n in[*open(0)][1:]:
 s='';n=int(n)
 while n:s=str(n%3)+s;n//=3
 print(s or 0)