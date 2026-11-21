X,*l=map(str.split,open(0))
print('NYOE S'[all(X[1]in i for i in l[2::2])::2])