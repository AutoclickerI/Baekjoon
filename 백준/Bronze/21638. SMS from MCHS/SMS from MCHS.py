A,B=map(int,input().split())
C,D=map(int,input().split())
if C<0 and D>9:print('A storm warning for tomorrow! Be careful and stay home if possible!')
elif A>C:print('MCHS warns! Low temperature is expected tomorrow.')
elif D>B:print('MCHS warns! Strong wind is expected tomorrow.')
else:print('No message')