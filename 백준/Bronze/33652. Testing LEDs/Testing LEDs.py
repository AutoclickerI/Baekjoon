l=[i for i,j in[*map(str.split,open(0))][1:]if'1'>j]
print(min(l or[-1],key=int))