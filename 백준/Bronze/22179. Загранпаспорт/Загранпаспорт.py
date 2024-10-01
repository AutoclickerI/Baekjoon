def time_to_minutes(hh, mm):
    return hh * 60 + mm

def minutes_to_time(minutes):
    hh = minutes // 60
    mm = minutes % 60
    return f"{hh:02}:{mm:02}"

def can_get_passport(start_time, windows):
    current_time = start_time
    
    for opening, closing, service_time in windows:
        opening_minutes = time_to_minutes(*map(int, opening.split(':')))
        closing_minutes = time_to_minutes(*map(int, closing.split(':')))
        
        # Determine when the service can start
        if current_time < opening_minutes:
            # Wait until the window opens
            current_time = opening_minutes
            
        # Check if the service can be started
        if current_time + service_time > closing_minutes:
            # Cannot start service, return No
            return False, None
        
        # Update current time to when service finishes
        current_time += service_time
    
    return True, current_time

# Read input
arrival_time_str = input().strip()
n = int(input().strip())
windows = []

for _ in range(n):
    # Read each window's details
    window_info = input().strip().split()
    opening = window_info[0]
    closing = window_info[1]
    service_time = int(window_info[2])
    windows.append((opening, closing, service_time))

# Parse arrival time
hh, mm = map(int, arrival_time_str.split(':'))
start_time = time_to_minutes(hh, mm)

# Process windows and determine if the passport can be obtained
success, finish_time = can_get_passport(start_time, windows)

# Output results
if success:
    print("Yes")
    print(minutes_to_time(finish_time))
else:
    print("No")