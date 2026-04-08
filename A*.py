#Use A* once at the start (or when replanning) to find the optimal route through the known grid 
import heapq

def heuristic(a, b):
    return abs(a[0]-b[0]) + abs(a[1]-b[1])  # Manhattan distance for grid

def astar(grid, start, goal):
    open_set = [(0, start)]
    came_from = {}
    g = {start: 0}

    while open_set:
        _, current = heapq.heappop(open_set)
        if current == goal:
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            return path[::-1]

        for dx, dy in [(0,1),(1,0),(0,-1),(-1,0),(1,1),(-1,1),(1,-1),(-1,-1)]:
            nb = (current[0]+dx, current[1]+dy)
            if 0 <= nb[0] < GRID_SIZE and 0 <= nb[1] < GRID_SIZE and grid[nb[1]][nb[0]] == 0:
                new_g = g[current] + (1.4 if dx and dy else 1)
                if nb not in g or new_g < g[nb]:
                    g[nb] = new_g
                    f = new_g + heuristic(nb, goal)
                    heapq.heappush(open_set, (f, nb))
                    came_from[nb] = current
    return []  # In the event that no path is found
