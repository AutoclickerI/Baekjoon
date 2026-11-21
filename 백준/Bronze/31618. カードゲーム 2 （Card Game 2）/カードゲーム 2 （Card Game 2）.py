d={*map(int,[*open(0)][1].split())}
print('YNeos'[all({i+3,i+6}-d for i in d)::2])