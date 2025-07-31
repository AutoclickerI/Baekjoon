a=[[*map(int,('-'+i).split())]for i in open(0)][1:]
print(a.index(min(a))+1)