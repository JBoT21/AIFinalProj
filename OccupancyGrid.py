#All three algorithms operate on the same 2D grid
import numpy as np

GRID_SIZE = 5   # Just choosing a value, idk if 5 is good or not
CELL_CM   = 10   # each cell = 10 cm (idk, just picking a number)

grid = np.zeros((GRID_SIZE, GRID_SIZE), dtype=np.uint8)
# 0 = free, 1 = obstacle, 2 = unknown

def update_grid(robot_pos, distance_cm, heading_deg):
    #Mark obstacle cell from sonar reading.
    rad = np.radians(heading_deg)
    ox = robot_pos[0] + int(distance_cm * np.cos(rad) / CELL_CM)
    oy = robot_pos[1] + int(distance_cm * np.sin(rad) / CELL_CM)
    if 0 <= ox < GRID_SIZE and 0 <= oy < GRID_SIZE:
        grid[oy][ox] = 1