l=["white Barabashka", "blue book", "red chair", "gray mouse", "green bottle"]

for _ in range(5):
    s = input().replace("'", " ").replace(",", " ").replace(".", " ").replace("-", " ").split()
    word = [item for item in l if item in " ".join(s)]
    if len(word)-1:
        word = [item for item in l if item.split()[0] not in s and item.split()[1] not in s]
    print(word[0])