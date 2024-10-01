devices = [
    ("iPad Mini", 319, 1024, 768),
    ("Galaxy Tab", 419, 1024, 600),
    ("iPhone 4S", 450, 960, 640),
    ("iPad4", 519, 2048, 1536),
    ("iPhone 5C", 599, 1136, 640),
    ("Galaxy Tab2", 600, 1280, 800),
    ("Galaxy S4", 630, 1080, 1920),
    ("iPhone 5S", 719, 1136, 640),
]

def check(W, H, a, b):
    
    s = int(a * H / W) / b
    t = int(b * W / H) / a

    if a * H == b * W:
        return max(s, t)
    else:
        return min(s, t)

while'1'<(s:=input()):
    W, H = sorted(map(int,s.split()))
    print(min([(-max(check(H, W, a, b), check(W, H, a, b)), c) for _, c, a, b in devices])[1])