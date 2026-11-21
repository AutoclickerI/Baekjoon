while'0'<(s:=input()):
 a=0;l=len(s)
 while s!=s[::-1]:a+=1;s=str(int(s)+1).zfill(l)
 print(a)