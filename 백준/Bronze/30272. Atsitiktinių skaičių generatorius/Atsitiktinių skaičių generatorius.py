s='''
..#####..  ....##...  .#######.  .#######.  ##.......
.##...##.  ..####...  ##.....##  ##.....##  ##....##.
##.....##  ....##...  .......##  .......##  ##....##.
##.....##  ....##...  .#######.  .#######.  ##....##.
##.....##  ....##...  ##.......  .......##  #########
.##...##.  ....##...  ##.......  ##.....##  ......##.
..#####..  ..######.  #########  .#######.  ......##.
.........  .........  .........  .........  .........
.########  .#######.  .########  .#######.  .#######.
.##......  ##.....##  .##....##  ##.....##  ##.....##
.##......  ##.......  .....##..  ##.....##  ##.....##
.#######.  ########.  ....##...  .#######.  .########
.......##  ##.....##  ...##....  ##.....##  .......##
.##....##  ##.....##  ...##....  ##.....##  ##.....##
..######.  .#######.  ...##....  .#######.  .#######.
.........  .........  .........  .........  .........
'''.split()
d={}
for idx in range(5):
    t=tuple(''.join(i)for i in s[1*idx:1*idx+40:5])
    d[t]=idx
for idx in range(5):
    t=tuple(''.join(i)for i in s[40+1*idx:1*idx+80:5])
    d[t]=idx+5
for _ in[0]*int(input()):
    print(end=str(d[tuple(input()for _ in[0]*8)]))