I=0
for i in[*open(0)][1:]:I+=1;p,q,r=map(int,i.split());print(f'Case #{I}:',sum(j&k<r for j in range(p)for k in range(q)))