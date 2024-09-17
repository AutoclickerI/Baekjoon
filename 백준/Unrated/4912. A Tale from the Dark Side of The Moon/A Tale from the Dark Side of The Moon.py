s=open(0).read().replace('cei',chr(1000)).replace('dd','p').replace('pink','floyd').replace('ei','ie').split('EOF')[0].replace(chr(1000),'cei')
for i in s:
    if i.islower()or i in' \n':print(end=i)