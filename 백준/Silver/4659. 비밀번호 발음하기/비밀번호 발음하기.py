v={*'aeiou'}
z={*'qzwsxdcrfvtgbyhnjmklp'}
for s in[*open(0)][:-1]:
    s=s[:-1]
    a='not '
    if {*s}&{*'aeiou'} and all(not({i,j,k}<=v or{i,j,k}<=z)for i,j,k in zip(s,s[1:],s[2:]))and all(not('e'!=i==j!='o')for i,j in zip(s,s[1:])):
        a=''
    print(f'<{s}> is',a+'acceptable.')