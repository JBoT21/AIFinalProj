# Note to self:  run this from ~/TurboPi/turbopi_nav/
import sys, os, time, numpy as np

sys.path.append('/home/pi/TurboPi/')

from driver  import move, stop, get_distance
from OccupancyGrid      import grid, update_grid
from AStar     import astar
from QLearn import Q, choose_action, update_q, get_state, get_reward, ACTIONS
from DynamicWindowApproach import dwa_control
from nav import navigate

START = (0, 0) #Change this to actual starting position
GOAL  = (5, 5) #Change this to actual goal position
Q_PATH = "qtable.npy"

def load_q():
    global Q
    if os.path.exists(Q_PATH):
        Q[:] = np.load(Q_PATH)
        print(f"Loaded Q-table from {Q_PATH}")
    else:
        print("Starting with fresh Q-table")

def save_q():
    np.save(Q_PATH, Q)
    print(f"Q-table saved to {Q_PATH}")

if __name__ == "__main__":

    load_q()
    try:
        navigate(
            start      = START,
            goal       = GOAL,
            grid       = grid,
            move_fn    = move,
            stop_fn    = stop,
            dist_fn    = get_distance,
            astar_fn   = astar,
            dwa_fn     = dwa_control,
            q_fns      = (choose_action, update_q, get_state, get_reward, ACTIONS),
        )
    except KeyboardInterrupt:
        print("Navigation interrupted by user.")
    finally:
        stop()
        save_q()
        print("Exiting program.")