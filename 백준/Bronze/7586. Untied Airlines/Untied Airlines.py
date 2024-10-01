def calculate_upgrades():

    # Mapping of service problem codes to their respective points
    points_map = {
        'L': 120,  # Lost Luggage
        'S': 150,  # Struck by Stewardess
        'B': 150,  # Overbooked and bumped off flight after checking in
        'N': 40,   # Not greeted by name
        'C': 160,  # Not given seat in class paid for
        'D': 100,  # Drinks trolley ran into passenger
        'R': 100,  # Stewardess rude
        'O': 100   # No space in overhead locker
    }

    result = []

    while True:
        flight_number = input()
        if flight_number == "#":
            break

        d={}
        while True:
            seat_info = input()
            if seat_info == "00A":
                break
            
            # Get the service code, which is the last character
            seat,service_code = seat_info.split()
            if service_code in points_map:
                d[seat] = d.get(seat,0)+points_map[service_code]
            
        
        result.append(f"{flight_number} {sum(i>=200 for i in d.values())}")

    # Print results for all flights
    for line in result:
        print(line)

# Call the function to start processing
calculate_upgrades()