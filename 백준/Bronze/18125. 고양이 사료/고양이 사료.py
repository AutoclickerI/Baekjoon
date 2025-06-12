[R,C],*l=[(*map(int,i.split()),)for i in open(0)]
o=[i[::-1]for i in zip(*l[:C])]
z=l[C:]
if o==z:print(r'''|>___/|        /}
| O < |       / }
(==0==)------/ }
| ^  _____    |
|_|_/     ||__|''')
else:print(r'''|>___/|     /}
| O O |    / }
( =0= )""""  \
| ^  ____    |
|_|_/    ||__|''')