s,k=open(c:=0,'rb')
for i in s:print(end=[' ',chr((i+~k[c%~-len(k)])%26+97)][40<i]);c+=1