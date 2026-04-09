"""Q-learning handles the dynamic, unpredictable parts (
new obstacles, narrow gaps) that A* can't anticipate
"""

import numpy as np, random

ACTIONS = ['forward', 'left', 'right', 'back']
Q = np.zeros((4, 4))   # 4 sonar states × 4 actions

def get_state(dist):
    if dist < 15:  return 0  # danger
    if dist < 30:  return 1  # caution
    if dist < 60:  return 2  # clear
    return 3                 # open

def choose_action(state, epsilon=0.1):
    if random.random() < epsilon:
        return random.randint(0, 3)
    return int(np.argmax(Q[state]))

def update_q(s, a, r, s_next, alpha=0.1, gamma=0.9):
    Q[s, a] += alpha * (r + gamma * np.max(Q[s_next]) - Q[s, a])

def get_reward(dist, reached_goal=False):
    if reached_goal:   return +100
    if dist < 15:      return -50   #risk of colliding with obstacle
    if dist < 30:      return -10
    return +1                       # good progress