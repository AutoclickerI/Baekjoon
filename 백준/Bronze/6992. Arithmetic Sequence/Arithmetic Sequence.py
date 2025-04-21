for i in[*open(0)][1:]:
    _,*l=map(int,i.split());v,*z={j-i for i,j in zip(l,l[1:])}
    if z:print('The sequence',l,'is not an arithmetic sequence.')
    else:print('The next 5 numbers after',l,'are:',[*range(l[-1]+v,l[-1]+v*6,v)])