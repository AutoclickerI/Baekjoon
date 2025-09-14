l=[]
for i in[*open(0)][1:]:
    if'R'<i:l+=i[4:-1],
    else:l+=l.pop(~(i.count('+')%len(l))),
    print(l[-1])