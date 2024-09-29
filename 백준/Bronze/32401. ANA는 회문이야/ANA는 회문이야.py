input()
s=input()
if'A'not in s:
    print(0)
else:
    print(sum(i.count('N')==1 for i in s[s.find('A'):s.rfind('A')+1].split('A')))