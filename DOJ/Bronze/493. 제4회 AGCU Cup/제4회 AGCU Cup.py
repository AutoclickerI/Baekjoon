A,G,C,U=map(input().__contains__,'AGCU')
print(A|G<<1|C<<2|U<<3)