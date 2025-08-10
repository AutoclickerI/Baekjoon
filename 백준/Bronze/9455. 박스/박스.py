_,*l=open(0)
while l:r=int(l.pop(0).split()[0]);print(sum(('0'<b[j])*b[j+1:].count('0')for b in zip(*l[:r])for j in range(r)));l=l[r:]