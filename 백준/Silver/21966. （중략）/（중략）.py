S=[*open(0)][1]
if len(S)<27:print(S)
elif'.'in S[11:-13]:print(S[:9]+'.'*6+S[-11:])
else:print(S[:11]+'...'+S[-12:])