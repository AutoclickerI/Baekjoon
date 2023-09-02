*l,_=open(0)
while l:p,q=map(int,l.pop(0).split());print(sum(min(i,q//p)for i in map(int,l.pop(0).split())))