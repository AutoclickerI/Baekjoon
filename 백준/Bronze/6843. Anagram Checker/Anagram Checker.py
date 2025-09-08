f=lambda:sorted(input().replace(' ',''))
print('Is',*['not','an anagram.'][f()==f():])