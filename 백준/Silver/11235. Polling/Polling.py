from statistics import*
print(*sorted(multimode([l for l in open(0)][1:])),sep='')