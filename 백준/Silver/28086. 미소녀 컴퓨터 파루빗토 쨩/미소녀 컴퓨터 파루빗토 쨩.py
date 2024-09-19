f=1
s=''
for i in input():
    if f and'0'<i<':':
        s+='0o'
        f=0
    if i in'+-*/':
        f=1
    s+=i
try:
    print('%o'%eval(s.replace('/','//')))
except:
    print('invalid')