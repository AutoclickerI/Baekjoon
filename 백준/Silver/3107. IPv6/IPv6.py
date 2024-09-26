s=input()
if'::'in s:s=s.replace('::',':'*(7-s.count(':')+2))
print(':'.join(('0000'+i)[-4:]for i in s.split(':')))