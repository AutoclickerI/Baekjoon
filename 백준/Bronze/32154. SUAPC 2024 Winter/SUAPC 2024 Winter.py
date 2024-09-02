z='ACEFGHLM'
s=[z+'BDJ',*[z+'I']*2,z+'B',*[z]*5,'ABCFGHLM'][int(input())-1]
print(len(s),*sorted(s))