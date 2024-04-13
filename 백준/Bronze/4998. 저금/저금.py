for i in open(0):
 n,b,m=map(eval,i.split());c=0
 while n<m:n*=1+b/100;c+=1
 print(c)