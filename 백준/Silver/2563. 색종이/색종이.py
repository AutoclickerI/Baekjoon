l=set()
for I in[*open(0)][1:]:p,q=map(int,I.split());l|={(i//10+p,i%10+q)for i in range(100)}
print(len(l))