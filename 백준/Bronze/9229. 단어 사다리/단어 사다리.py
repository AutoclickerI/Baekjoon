while 1:
 a=[]
 while(i:=input())>'#':a+=i,
 a or exit()
 print(('C','Inc')[any(len(b)!=len(c)or 1!=len({*b}-{*c})for b,c in zip(a,a[1:]))]+'orrect')