d={'Paper':57.99,'Printer':120.50,'Planners':31.25,'Binders':22.50,'Calendar':10.95,'Notebooks':11.20,'Ink':66.95}
print(f'${sum(d[i]for i in open(0).read().split()[:-1]):.2f}')