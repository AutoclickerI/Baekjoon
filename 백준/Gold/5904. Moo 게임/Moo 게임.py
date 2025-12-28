n=int(input())-1
i=max(n//4-9,0)
while(v:=i*4-i.bit_count())<n:i+=1
print('om'[v==n])