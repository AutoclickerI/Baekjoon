s=input()
if s==s.lower()and'__'not in s and s[-1]!='_'!=s[0]:
    print(s[0]+''.join(i.capitalize()for i in s.split('_'))[1:])
elif'_'not in s and not s[0].isupper():
    r=''
    for i in s:
        r+='_'*i.isupper()+i.lower()
    print(r)
else:
    print('Error!')