s=input()
print('in'*(int(''.join(str(int(x,36))for x in s[4:]+s[:4]))%97!=1)+'correct')