import re
p,t=map(int,input().split())
print(['ALL INFECTED','CURED']['H'in re.sub('H{0,%d}IH{0,%d}'%((~-t//p,)*2),'',input())])