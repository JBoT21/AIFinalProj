"""This is where all three algorithms work together: 
  A* sets the destination, Q-learning handles the moment-to-moment decisions, and
  DWA smooths the moment-to-moment driving
"""

import time, numpy as np

def navigate(start, goal, grid, move_fn, stop_fn, dist_fn,
             astar_fn, dwa_fn, q_fns):

    choose_action, update_q, get_state, get_reward, ACTIONS = q_fns
    robot_pos = list(start)
    path = astar_fn(grid, tuple(start), goal)
    waypoint_idx = 0

    print(f"[Nav] Path found: {len(path)} waypoints")

    while waypoint_idx < len(path):
        dist  = dist_fn()
        state = get_state(dist)

        if dist < 20:
            action_idx = choose_action(state)
            action     = ACTIONS[action_idx]
            if   action == 'left':  move_fn(40, -0.6)
            elif action == 'right': move_fn(40,  0.6)
            elif action == 'back':  move_fn(-40, 0)
            else:                   move_fn(60, 0)

            new_dist = dist_fn()
            update_q(state, action_idx, get_reward(new_dist), get_state(new_dist))

        else:
            wp       = path[waypoint_idx]
            goal_dir = np.arctan2(wp[1]-robot_pos[1], wp[0]-robot_pos[0])
            speed, turn = dwa_fn(60, goal_dir, dist)
            move_fn(speed, turn)

            if abs(robot_pos[0]-wp[0]) < 2 and abs(robot_pos[1]-wp[1]) < 2:
                waypoint_idx += 1
                print(f"[Nav] Waypoint {waypoint_idx}/{len(path)}")

        time.sleep(0.1)

    stop_fn()
    print("Goal reached!")