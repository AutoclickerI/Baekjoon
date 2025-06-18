k=int(input())
i=0
while 9<k:k=sum(map(int,str(k)));i+=1
print(i,'YNEOS'[0<k%3::2])