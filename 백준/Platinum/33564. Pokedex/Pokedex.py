import sys
input=sys.stdin.readline

class pokemon:
    idx=1
    def __init__(self,name,type1,type2,hp,atk,deff,special_atk,special_def,speed):
        *self.data,=map(int,[pokemon.idx,hp,atk,deff,special_atk,special_def,speed])
        pokemon.idx+=1
        self.name=name
        self.type1=type1
        self.type2=type2
    def __repr__(self):
        return f'pokemon({self.data[0]})'

filter_type={*'bug dark dragon electric fairy fighting fire flying ghost grass ground ice normal poison psychic rock steel water'.split()}
filter_name=''
filter_sp=[[1,200000]for _ in[0]*7]

idxs='idx hp atk def special_atk special_def speed'.split()

W=H=5

cursor=0

cursors=[('up',W,H)]

pokemons=[]

fibot=[0]*7
idx=[0]*7

def permute(v):
    return[fibot[i]*v[i]for i in s]

for _ in[0]*int(input()):
    pokemons+=pokemon(*input().split()),

for ii in range(1,int(input())+1):
    q,*l=input().split()
    if q=='flush':
        s=[i for i in sorted(range(7),key=lambda i:-idx[i])if fibot[i]]
        pokemons.sort(key=lambda i:permute(i.data))
        fibot=[0]*7
        idx=[0]*7
        l=[]
        for p in pokemons:
            if(p.type1 in filter_type or p.type2 in filter_type) and (filter_name==''or p.name.startswith(filter_name))and all(j<=i<=k for i,(j,k)in zip(p.data,filter_sp)):
                l+=p,
        for i in cursors:
            if i[0]=='up':
                tW,tH=i[1],i[2]
                continue
            if i=='l':
                cursor=max(0,cursor-1)
            if i=='r':
                cursor=min(len(l)-1,cursor+1)
            if i=='u':
                cursor=max(0,cursor-tW)
            if i=='d':
                cursor=min(len(l)-1,cursor+tW)
        cursors=[('up',W,H)]
        p=[p.data[0] for p in l[cursor//W*W:]]+[0]*200
        for i,_ in zip(zip(*[iter(p)]*W),range(H)):
            print(*i)
        print()
    elif q=='cursor':
        cursors+=l
    elif q=='sort':
        v=idxs.index(l[0])
        fibot[v]=(l[1]=='asc')*2-1
        idx[v]=ii
        
        cursors=[('up',W,H)]
        cursor=0
    elif q=='resize':
        if l[0]=='W':
            W=int(l[1])
        else:
            H=int(l[1])
        cursors+=('up',W,H),
    elif q=='filter':
        if l[0]=='name':
            if l[1]=='BLANK':
                filter_name=''
            else:
                filter_name=l[1]
        elif l[0]=='type':
            filter_type^={l[1]}
        else:
            filter_sp[idxs.index(l[0])][l[1]=='max']=int(l[2])
        cursors=[('up',W,H)]
        cursor=0
    else:
        raise