def find_best_meeting_date(test_cases):
    results = []
    
    for case in test_cases:
        N, Q = case[0]
        if N == 0 and Q == 0:
            break
        
        # Dictionary to count how many members are available on each date
        date_counts = {}
        
        # Process each member's convenient dates
        for member_dates in case[1]:
            for date in member_dates:
                if date not in date_counts:
                    date_counts[date] = 0
                date_counts[date] += 1
        
        # Find the best date that meets the quorum and has the most members
        best_date = 0
        max_members = 0
        
        for date, count in sorted(date_counts.items()):
            if count >= Q and count > max_members:
                best_date = date
                max_members = count
        
        # If no date meets the quorum, return 0
        if max_members == 0:
            results.append(0)
        else:
            results.append(best_date)
    
    return results

# Input Parsing
def parse_input():
    test_cases = []
    
    while True:
        first_line = list(map(int, input().split()))
        if first_line == [0, 0]:
            break
        N, Q = first_line
        members = []
        
        for _ in range(N):
            member_input = list(map(int, input().split()))[1:]  # Skip M and get the dates
            members.append(member_input)
        
        test_cases.append(((N, Q), members))
    
    return test_cases

# Read and process the input
test_cases = parse_input()
results = find_best_meeting_date(test_cases)

# Output results
for result in results:
    print(result)