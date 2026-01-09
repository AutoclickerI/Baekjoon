I=input
exec("l=I().split()\nwhile'?'<(i:=I())[-1]:l=[j for j in l if i.split()[-1]!=j]\nprint(*l);"*int(I()))