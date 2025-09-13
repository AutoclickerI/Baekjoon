s='C C# D D# E F F# G G# A A# B'.split()
d={s[i]:{s[(i+j)%12]for j in(0,2,4,5,7,9,11)}for i in range(12)}
for i in[*open(0)][:-1]:print(*[c for c in d if{*i.split()}<=d[c]])