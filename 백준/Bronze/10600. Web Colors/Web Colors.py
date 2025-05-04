class color:
    def __init__(self,s,r,g,b):
        self.s=s
        self.l=[r,g,b]
    def __str__(self):
        return self.s
    def __sub__(self,x):
        return sum((i-j)**2 for i,j in zip(self.l,x))

c=[color('White',255,255,255),
 color('Silver',192,192,192),
 color('Gray',128,128,128),
 color('Black',0,0,0),
 color('Red',255,0,0),
 color('Maroon',128,0,0),
 color('Yellow',255,255,0),
 color('Olive',128,128,0),
 color('Lime',0,255,0),
 color('Green',0,128,0),
 color('Aqua',0,255,255),
 color('Teal',0,128,128),
 color('Blue',0,0,255),
 color('Navy',0,0,128),
 color('Fuchsia',255,0,255),
 color('Purple',128,0,128)]

for i in[*open(0)][:-1]:
    *l,=map(int,i.split())
    print(min(c,key=lambda i:i-l))