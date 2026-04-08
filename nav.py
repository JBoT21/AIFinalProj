"""This is where all three algorithms work together: 
  A* sets the destination, Q-learning handles the moment-to-moment decisions, and
  DWA smooths the moment-to-moment driving
"""

def navigate(start, goal):
    robot_pos = list(start)
    path = astar(grid, tuple(start), goal)
    waypoint_idx = 0

    while waypoint_idx < len(path):
        dist = get_distance()
        state = get_state(dist)

        if dist < 20:
            # Danger zone — let Q-learning react
            action_idx = choose_action(state, epsilon=0.05)
            action = ACTIONS[action_idx]
            if   action == 'left':  move(40, -0.6)
            elif action == 'right': move(40,  0.6)
            elif action == 'back':  move(-40, 0)
            else:                   move(60, 0)

            new_dist = get_distance()
            reward = get_reward(new_dist)
            update_q(state, action_idx, reward, get_state(new_dist))

        else:
            # Open space — follow A* via DWA
            wp = path[waypoint_idx]
            goal_dir = np.arctan2(wp[1]-robot_pos[1], wp[0]-robot_pos[0])
            speed, turn = dwa_control(60, goal_dir, dist)
            move(speed, turn)

            # Advance waypoint when close enough
            if abs(robot_pos[0]-wp[0]) < 2 and abs(robot_pos[1]-wp[1]) < 2:
                waypoint_idx += 1

        time.sleep(0.1)

    stop()
    print("Goal reached!")