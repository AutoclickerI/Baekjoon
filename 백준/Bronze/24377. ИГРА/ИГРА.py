s=input()[::2]
print(*[s[:2],[s.find('0')+1,10-eval('+'.join(s))],sorted({*'1234'}-{*s})][s.count('0')])