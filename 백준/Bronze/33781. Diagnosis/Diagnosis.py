def main():
    import sys
    input = sys.stdin.readline
    
    # Read first line: number of diseases and symptoms.
    n, m = map(int, input().split())
    
    # Read the diagnosed diseases.
    diagnosed_info = list(map(int, input().split()))
    k = diagnosed_info[0]
    diagnosed_diseases = diagnosed_info[1:]
    
    # Build a set to accumulate symptoms from diagnosed diseases.
    union_symptoms = set()
    
    # Read each disease's symptoms.
    disease_symptoms = []
    for _ in range(n):
        data = list(map(int, input().split()))
        p = data[0]
        symptoms = data[1:]
        disease_symptoms.append(set(symptoms))
    
    # For each diagnosed disease, union the symptom sets.
    for disease_index in diagnosed_diseases:
        # Disease indices are 1-indexed.
        union_symptoms |= disease_symptoms[disease_index - 1]
    
    # Compare the union with the complete set of symptoms.
    if union_symptoms == set(range(1, m + 1)):
        print("yes")
    else:
        print("no")
        
if __name__ == "__main__":
    main()