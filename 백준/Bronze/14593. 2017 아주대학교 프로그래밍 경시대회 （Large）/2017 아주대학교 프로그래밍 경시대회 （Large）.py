a=[eval(i.replace(' ',',-'))for i in open(0)][1:]
print(a.index(max(a))+1)