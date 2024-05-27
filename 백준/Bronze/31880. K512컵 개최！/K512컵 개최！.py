_,q,r=open(0)
print(eval(q.replace(*' +'))*eval('*'.join(i for i in r.split()if'0'!=i)or'1'))