for i in[*open(0)][1:]:a,b,c=map(int,i.split());c*=c;print(max(a*b//c+(a*b%c*2>c),1)*c)