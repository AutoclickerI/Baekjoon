from collections import Counter
for i in range(int(input())):
    vote = Counter({"cinema": 0, "cocktail bar": 0, "disco": 0})
    names={*input().split()}
    for name in names:
        match name:
            case "Anne":vote["cinema"] += 1
            case "Bob":
                vote["disco"]+="Karin" in names and "Dave" not in names and "Edward" not in names and "Anne" in names
                vote["cocktail bar"] +="Karin" not in names and ("Dave" in names or "Edward" in names or "Anne" not in names)
            case "Karin":
                if "Charly" in names:vote["disco"] += 1
                elif "Anne" in names:vote["cinema"] += 1
                else:vote["cocktail bar"] += 1
            case "Charly":vote["cinema"]+="Anne" in names
            case "Edward":
                if "Anne" in names and "Charly" not in names:vote["cocktail bar"] += 1
                else:vote["cinema"] += 1
            case "Frank":
                if "Bob" not in names and "Anne" not in names:vote["cinema"] += 1
                elif "Anne" in names:vote["disco"] += 1
    print(f"Scenario #{i+1}:")
    a, b = vote.most_common(2)
    if a[1]==b[1]:
        print("stay at the Hacienda")
    else:
        print(a[0])
    print()