for i in[*open(0)][1:]:_,*l=map(int,i.split());print('YNEOS'[any(i+j-k for i,j,k in zip(l,l[1:],l[2:]))::2])