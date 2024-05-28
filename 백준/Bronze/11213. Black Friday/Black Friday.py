s=[*open(0)][1].split()
print([*max(1//s.count(i)*[i,s.index(i)+1]for i in s),0,'none'][1])