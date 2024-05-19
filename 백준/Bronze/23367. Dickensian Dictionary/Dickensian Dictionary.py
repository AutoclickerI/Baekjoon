x=[i in'yuiophjklnm'for i in input()]
print('nyoe s'[all(i^j for i,j in zip(x,x[1:]))::2])