for i in[*open(0)][1:]:
 n,s=int(i),''
 while n:s=chr(~-n%26+65)+s;n=~-n//26
 print(s)