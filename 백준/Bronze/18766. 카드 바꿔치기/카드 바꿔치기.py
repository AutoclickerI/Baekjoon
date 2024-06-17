f=lambda:sorted(input().split())
exec("f();print('NOT '*(f()==f())+'CHEATER');"*int(f()[0]))