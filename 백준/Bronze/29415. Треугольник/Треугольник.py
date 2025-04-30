s=int(input())*2
print(sum(s%x==0==(x**2+(s/x)**2)**.5%1for x in range(1,s+1))//2)