b,*l=input().split()
for i in l:
    i=i[:-1]
    s=''
    while i[-1]in'*&]':
        s+=i[-1-(i[-1]==']'):]
        i=i[:-1-(i[-1]==']')]
    print(b+s,i+';')