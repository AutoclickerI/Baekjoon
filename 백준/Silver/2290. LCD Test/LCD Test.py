s='''      --   --        --   --   --   --   --   --  
   |    |    | |  | |    |       | |  | |  | |  | 
   |    |    | |  | |    |       | |  | |  | |  | 
      --   --   --   --   --        --   --       
   | |       |    |    | |  |    | |  |    | |  | 
   | |       |    |    | |  |    | |  |    | |  | 
      --   --        --   --        --   --   --  '''.split('\n')
s=*s[:2],s[3],*s[5:]
d=[[i[j:j+4][:2]+i[j+3]for i in s]for j in range(0,len(s[0]),5)]


s,n=input().split()
t=[]
for i in d:
    z=[j[0]+j[1]*int(s)+j[2]for j in i]
    t+=[z[0]]+[z[1]]*int(s)+[z[2]]+[z[3]]*int(s)+[z[4]],
t=t.pop(),*t
a=[''for _ in[0]*len(t[0])]
for i in n:
    c=t[int(i)]
    for j in range(len(t[0])):
        a[j]+=c[j]+' '
for i in a:print(i[:-1])