while int(s:=input()):
 while s[1:]:print(s);s=str(eval('*'.join(s)))
 print(s)