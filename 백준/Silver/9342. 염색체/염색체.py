import re
l=re.compile('^[ABCDEF]?A+F+C+[ABCDEF]?$')
exec("print(l.match(input())and'Infected!'or'Good');"*int(input()))