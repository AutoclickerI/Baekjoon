def diff(a,b):
    ci=sum(i==j for i,j in zip(a,b))
    sq=sum(min(b.count(i),a.count(i))for i in{*a})
    return ci,sq-ci

for _ in[0]*int(input()):
    a,b=input().split()
    ci,sq=diff(('0'*3+a)[-4:],('0'*3+b)[-4:])
    print(f'For secret = {a} and guess = {b}, {ci} circles and {sq} squares will light up.')