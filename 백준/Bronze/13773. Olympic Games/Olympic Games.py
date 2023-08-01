while s:=int(input()):
    t=s//4
    if s%4 or t<474:print(s,'No summer games')
    elif t==479 or t==485 or t==486:print(s,'Games cancelled')
    elif t>505:print(s,'No city yet chosen')
    else:print(s,'Summer Olympics')