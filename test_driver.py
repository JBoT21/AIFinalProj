import time
from driver import move, stop, get_distance, move_forward, turn_left, turn_right

print("Testing TurboPi driver...")

# Test distance sensor
print(f"Distance: {get_distance()} cm")

# Test forward movement
print("Moving forward...")
move_forward(30)
time.sleep(2)
stop()

# Test turning
print("Turning left...")
turn_left(30)
time.sleep(1)
stop()

print("Turning right...")
turn_right(30)
time.sleep(1)
stop()

print("Test complete!")