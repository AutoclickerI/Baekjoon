from string import*
i=0
I=input
exec("i+=1;I();s=I()\nfor K in'#@*&',ascii_uppercase,ascii_lowercase,digits:s+=K[any(map(s.count,K)):1]\nprint(f'Case #{i}:',s+'_'*(7-len(s)));"*int(I()))