n=int(input())
a=2
x=[i for i in range(104)if all(i%j for j in range(2,i))]
while n>=x[a]*x[a:=a+1]:1
print(x[a]*x[a-1])