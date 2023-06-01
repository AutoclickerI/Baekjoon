a = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
d = input()
e = ''
for i in a:
    try:
        e += f'{list(d).index(i)} '
    except:
        e += '-1 '
print(e+' ')