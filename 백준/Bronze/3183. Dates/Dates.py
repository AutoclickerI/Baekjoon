from datetime import*
for s in[*open(0)][:-1]:
 try:date(*map(int,s.split()[::-1]));s='V'
 except:s='Inv'
 print(s+'alid')