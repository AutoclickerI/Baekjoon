d={1:"Yakk",2:"Doh",3:"Seh",4:"Ghar",5:"Bang",6:"Sheesh"}
for i in range(int(input())):
    p,q=sorted(map(int,input().split()))
    if p==q:print(f'Case {i+1}:',{1:'Habb Yakk',2:'Dobara',3:'Dousa',4:'Dorgy',5:'Dabash',6:'Dosh'}[p])
    elif p==5 and q==6:print(f'Case {i+1}:','Sheesh Beesh')
    else:print(f'Case {i+1}:',d[q],d[p])