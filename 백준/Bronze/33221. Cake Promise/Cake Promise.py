a,t,*l=[(len(l:=[int(i)for i in s.split()if'A'>i]),-sum(l))for s in open(0)]
print(sum(i>=t for i in l))