I=input
for s in[0]*int(I()):I();s=I();t=(ord(s[0])-ord(I()))%26;print(''.join(map(lambda s:chr(97+(ord(s)+7-t)%26),s)))