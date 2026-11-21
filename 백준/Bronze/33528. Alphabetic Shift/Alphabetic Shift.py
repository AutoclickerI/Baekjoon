s=input()
for i in range(26):print(''.join(chr(65+(ord(c)-i-65)%26)for c in s))