k='A A# B C C# D D# E F F# G G# A Bb Cb B# Db D Eb Fb E# Gb G Ab'.split()
for i,j in zip(*[open(0)]*2):print(*(k[(x+int(j))%12]for x in map(k.index,i.split())))