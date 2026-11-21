l=sorted(map(int,[*open(0)][1].split()))
o=l[::2]+l[1::2][::-1]
print(sum(i*j for i,j in zip(o,(2*o)[1:])),*o)