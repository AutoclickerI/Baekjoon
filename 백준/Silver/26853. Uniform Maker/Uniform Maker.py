i,*x=open(0)
print(eval(i.replace(' ','*-~'))-sum(max(map(l.count,l))for l in zip(*x)))