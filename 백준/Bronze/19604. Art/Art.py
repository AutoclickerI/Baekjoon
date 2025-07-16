x,y=zip(*map(eval,[*open(0)][1:]))
print(f'{min(x)-1},{min(y)-1} {max(x)+1},{max(y)+1}')