def check(n):
    return sum(i for i in range(1,n)if n%i<1)
def printer(n):
    if check(n)>n and all(check(i)<=i for i in range(1,n)if n%i<1):
        print("Good Bye")
    else:
        print("BOJ 2022")
for _ in[0]*int(input()):
    printer(int(input()))