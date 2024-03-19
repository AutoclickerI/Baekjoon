*s,=map(str.split,open(0))
print(1-all({*i}-{j}for*i,j in[*zip(*s)]+s))