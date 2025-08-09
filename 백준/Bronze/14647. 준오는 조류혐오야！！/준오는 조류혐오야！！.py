_,*l=open(0)
print(sum(z:=[i.count('9')for i in l])-max(z+[''.join(i).count('9')for i in zip(*map(str.split,l))]))