p,q=map(open(0).read().count,[s:='bigdata',S:='security'])
print((s+'? ')*(p>=q)+(S+'!')*(p<=q))