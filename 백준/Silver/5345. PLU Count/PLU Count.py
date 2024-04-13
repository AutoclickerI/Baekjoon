for i in[*open(0)][1:]:
 c=0
 for j in i:c+=j.lower()=='plu'[c%3]
 print(c//3)