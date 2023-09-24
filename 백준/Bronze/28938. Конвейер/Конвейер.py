s=sum(map(int,[*open(0)][1].split()))
print(['Stay','Right','Left'][(s>0)-(s<0)])