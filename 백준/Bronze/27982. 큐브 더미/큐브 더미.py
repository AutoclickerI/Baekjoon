s={eval('6*'+x.replace(' ','*6+'))for x in[*open(0)][1:]}
print(sum(all(s>{x-d,x+d}for d in[1,6,36])for x in s))