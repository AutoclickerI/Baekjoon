while'0'<(s:=input()):
 a=0
 while s!=s[::-1]:a+=1;s=str(int(s)+1).zfill(len(s))
 print(a)