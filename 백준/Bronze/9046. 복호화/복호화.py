for i in[*open(0)][1:]:
    *_,v,q=sorted('qazwsxedcrfvtgbyhnujmiklop',key=i.count)
    print('?'*(i.count(v)==i.count(q))or q)