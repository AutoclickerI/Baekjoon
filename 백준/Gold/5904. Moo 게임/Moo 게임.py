n=int(input())-1
i=n//5
while(v:=i*4-i.bit_count())<n:i+=1
print('om'[v==n])