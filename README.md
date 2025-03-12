# Elevator Travel Time Calculator

## How to Run

```
python elevator_calc.py start=<number> floor=<number>,<number>,...
```

Example:
```
python elevator_calc.py start=5 floor=2,8,10
```

## About

This script calculates how long an elevator takes to travel between different floors and shows the path it takes. It uses a simple model where each floor of travel takes 10 time units.

## Features

- Starts on floor 0 by default (can be changed with `start=` parameter)
- Travel time is 10 units per floor in any direction
- Visits floors in the exact order provided
- Returns total travel time and complete path taken

## Limitations

- No route optimization (doesn't find the shortest path)
- Basic input validation only
- No door opening/closing time calculations
- Single elevator only (no multi-elevator systems)
- No graphical visualization of movement