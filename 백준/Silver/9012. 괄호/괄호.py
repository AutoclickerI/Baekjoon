for i in[*open(0)][1:]:
 try:exec(i.replace(')','),'));print('YES')
 except:print('NO')