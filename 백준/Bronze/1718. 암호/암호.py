s,k=open(c:=0,'rb')
for i in s:print(end=i//97*chr((i+~k[c%~-len(k)])%26+97)or' ');c+=1