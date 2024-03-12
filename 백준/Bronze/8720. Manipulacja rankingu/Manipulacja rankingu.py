_,*l=[i.split()for i in open(0)]
print(1,sum([1^any(x=='100'!=s[i]for i,x in enumerate(l[0]))for s in l]))