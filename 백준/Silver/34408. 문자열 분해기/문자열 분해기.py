s,t=open(0)
print('NEED FIX'*any(s.count(i)<t.count(i)for i in t)or'OK')