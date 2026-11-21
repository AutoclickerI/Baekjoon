a='abcdefghijklmnopqrstuvwxyz'
d=input()
e=''
for i in a:
 try:e+=f'{list(d).index(i)} '
 except:e+='-1 '
print(e)