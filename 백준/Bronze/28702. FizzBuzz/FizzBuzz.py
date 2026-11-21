a=input()
b=input()
c=input()
def fizzbuzz(n):
    if n%15==0:
        return 'FizzBuzz'
    elif n%5==0:
        return 'Buzz'
    elif n%3==0:
        return 'Fizz'
    else:
        return n
if a.isdecimal():
    print(fizzbuzz(int(a)+3))
elif b.isdecimal():
    print(fizzbuzz(int(b)+2))
elif c.isdecimal():
    print(fizzbuzz(int(c)+1))