s=input()
print(*[eval(i.replace(*' +'))for i in[s.replace(*'65'),s.replace(*'56')]])