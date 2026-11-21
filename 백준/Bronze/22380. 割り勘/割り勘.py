*l,_=open(0)
while l:p,q,*l=l;p,q,*s=map(int,(p+q).split());print(sum(min(i,q//p)for i in s))