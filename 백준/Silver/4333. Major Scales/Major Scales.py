s='C C# D D# E F F# G G# A A# B'.split()
d={s[i]:{s[(i+j)%12]for j in b'`bdegik'}for i in range(12)}
for i in open(0):print(*[c for c in d if{*i.split()}<=d[c]])