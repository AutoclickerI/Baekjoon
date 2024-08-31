f=str.replace
s='('+f(f(f([*open(0)][1][:-1],')','))'),'(','(('),'+',')+(')+')'
print(len(s),s)