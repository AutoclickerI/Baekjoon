f=0
for i in open(0).read().lower():
    print(end=i.upper()if f else i)
    f|=i in'.?!'
    f&=i in'.?! ()\n'