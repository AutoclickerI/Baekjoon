l=[[*map(int,i.split())]for i in open(0)]
print((len({*[sum(i)for i in l]+[sum(i)for i in zip(*l)]})>1)*'not '+'magic')