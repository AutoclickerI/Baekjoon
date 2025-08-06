for i in[*open(0)][1:]:
 for R,G,B in zip(*[map(int,i.split())]*3):print(end='#o+-..'[(R*1063+G*3576+B*361)//255000])
 print()