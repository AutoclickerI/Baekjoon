print([S:=[*open(0)][1],[S[:11]+'...'+S[-12:],S[:9]+'.'*6+S[-11:]]['.'in S[11:-13]]][len(S)>26])