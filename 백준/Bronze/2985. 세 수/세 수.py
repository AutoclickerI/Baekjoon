l1=['+','-','/','*']
a,b,c=input().split()
try:
    for i in l1:
        if eval(a+'=='+b+i+c):
            print(a+'='+b+i+c)
            raise
        if eval(a+i+b+'=='+c):
            print(a+i+b+'='+c)
            raise
except:0