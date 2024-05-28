s=[*open(0)][1].split()
try:print(1+max([j,i]for i,j in enumerate(s)if s.count(j)<2)[1])
except:print('none')