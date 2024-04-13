for i in open(0):
 a,k={*map(str,range(10))},0
 while a:k+=1;a-={*str(int(i)*k)}
 print(k)