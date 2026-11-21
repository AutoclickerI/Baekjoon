s=[]
i=1
exec('s+=range(0,i*10,i);i+=1;'*9)
print(+(int(input())in s))