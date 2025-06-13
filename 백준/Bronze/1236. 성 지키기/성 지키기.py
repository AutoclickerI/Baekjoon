_,*l=open(0)
print(max(sum(map(lambda x:{*x}<={*'.\n'},i))for i in([*zip(*l)][:-1],l)))