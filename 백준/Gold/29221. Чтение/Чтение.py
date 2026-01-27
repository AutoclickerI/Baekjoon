l=open(0).read().lower().split()
if len(l)<l.count('the')*100:
    print('Real life')
else:
    print('Dreaming')