import sys

class Elevator:
    def __init__(self, start_floor=0):
        """Initialize with a starting floor."""
        self.current_floor = start_floor
        self.FLOOR_TRAVEL_TIME = 10 
        
    def calculate_travel_time(self, floors):
        """Calculate total travel time and path of visited floors."""
        total_time = 0
        current_position = self.current_floor
        visited_floors = [current_position]
        
        for next_floor in floors:
            distance = abs(next_floor - current_position)
            total_time += distance * self.FLOOR_TRAVEL_TIME
            current_position = next_floor
            visited_floors.append(next_floor)
            
        return total_time, visited_floors

def parse_arguments(args):
    """Parse command-line arguments for starting floor and floors to visit."""
    start_floor = 0
    floors_to_visit = []
    
    for arg in args:
        if arg.startswith("start="):
            start_floor = int(arg.split("=")[1])
                
        elif arg.startswith("floor="):
                floor_values = arg.split("=")[1].split(",")
                floors_to_visit = [int(floor) for floor in floor_values if floor.isdigit()]
        
    return start_floor, floors_to_visit

def main():
    """Process input, calculate travel time, and print the result."""
    args = sys.argv[1:]
    if not args:
        print("Usage: python elevator_calc.py start=<number> floor=<number>,<number>,...")
        sys.exit(1)
        
    start_floor, floors_to_visit = parse_arguments(args)
    elevator = Elevator(start_floor)
    total_time, visited_floors = elevator.calculate_travel_time(floors_to_visit)
    
    print(f"{total_time} {','.join(map(str, visited_floors))}")

if __name__ == "__main__":
    main()