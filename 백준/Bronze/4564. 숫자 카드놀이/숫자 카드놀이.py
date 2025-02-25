while int(s:=input()):
 while~-len(s):print(s);s=str(eval('*'.join(s)))
 print(s)