l=[*open(0)][1].split()
print('YNEOS'[len(l)==2 and int(l[0])>int(l[1])::2])