import re
print(re.sub(r' (PA|TE|N(I|ITI|EGO|O)|[AI](LI)?)?\b|\B.','',input().upper()))