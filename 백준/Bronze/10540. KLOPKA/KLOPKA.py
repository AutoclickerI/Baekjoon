print(max(map(lambda l:max(l)-min(l),zip(*[map(int,i.split())for i in open(0)][1:])))**2)