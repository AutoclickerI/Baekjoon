for s in[*open(0)][1:]:
 for i in range(65,91):s=s.replace(chr(i),'_'+chr(i+32))
 print(end=s.strip('_'))