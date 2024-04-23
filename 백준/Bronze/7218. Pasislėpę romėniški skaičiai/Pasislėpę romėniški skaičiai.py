s=[*open(0)][1]
l='I	II	III	IV	V	VI	VII	VIII	IX	X	XI	XII'.split()
for i in l:
    if i in s:print(l.index(i)+1,end=' ')