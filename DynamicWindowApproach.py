def dwa_control(robot_vel, goal_dir, dist_front):
    """Returns (speed, turn) avoiding obstacles."""
    best_score, best_cmd = -999, (0, 0)

    for v in np.linspace(20, 80, 5):      # speed candidates
        for w in np.linspace(-1, 1, 9):   # turn candidates
            # Predict position after 0.5s
            predicted_dist = dist_front - v * 0.5 * np.cos(w)
            if predicted_dist < 20:
                continue  # would hit something

            heading_score  = 1 - abs(w - goal_dir)
            velocity_score = v / 80
            clearance      = min(predicted_dist / 100, 1.0)
            score = 2*heading_score + velocity_score + 1.5*clearance

            if score > best_score:
                best_score = score
                best_cmd   = (v, w)
    return best_cmd
