for i in[*open(0)][:-1]:p,q,r=map(int,i[7:].split());F=p*372+q*31+r>11686;print([i[:6],'?'][F],p-F*30,q,r)