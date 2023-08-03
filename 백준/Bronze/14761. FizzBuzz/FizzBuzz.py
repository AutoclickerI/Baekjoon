a,b,c=map(int,input().split())
for i in range(1,c+1):
    if i%a==0==i%b:print('FizzBuzz')
    elif i%a==0:print('Fizz')
    elif i%b==0:print('Buzz')
    else:print(i)