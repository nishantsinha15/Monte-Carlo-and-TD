import numpy as np
import random
import matplotlib.pyplot as plt


# 0, 1, 2, 3 = up down left right
def q_init():
    q = [[{} for i in range(12)] for j in range(4)]
    for i in range(4):
        for j in range(12):
            for k in range(4):
                q[i][j][k] = -1
    for i in range(4):
        q[3][11][i] = 0
    return q


def epsilon_greedy(q, state, epsilon=0.1):
    if random.random() <= epsilon:
        return np.random.choice([0, 1, 2, 3])
    a, b = state
    ret = 0
    val = -1000000000
    for action in range(4):
        if q[a][b][action] > val:
            val = q[a][b][action]
            ret = action
    return ret


def move(state, action):
    if action == 0:
        next_state = state[0] - 1, state[1]
    if action == 1:
        next_state = state[0] + 1, state[1]
    if action == 2:
        next_state = state[0], state[1] - 1
    if action == 3:
        next_state = state[0], state[1] + 1

    if next_state == (3, 11):
        return next_state, 0
    elif next_state[0] == 3 and 1 <= next_state[1] <= 10:
        return (3, 0), -100
    elif 0 <= next_state[0] < 4 and 0 <= next_state[1] < 12:
        return next_state, -1
    else:
        return state, -1


def play_sarsa(q, alpha=0.1):
    state = 3, 0
    terminal_state = 3, 11
    action = epsilon_greedy(q, state)
    total_reward = 0
    while state != terminal_state:
        next_state, reward = move(state, action)
        total_reward += reward
        next_action = epsilon_greedy(q, next_state)
        a, b = state[0], state[1]
        c, d = next_state[0], next_state[1]
        q[a][b][action] = q[a][b][action] + alpha * (reward + q[c][d][next_action] - q[a][b][action])
        state = next_state
        action = next_action
    return total_reward


def sarsa():
    q = q_init()
    reward = []
    for episode in range(100):
        r = 0
        for runn in range(100):
            r += play_sarsa(q)
        reward.append(r / 100)
    return reward


def q_learning():
    q = q_init()
    reward = []
    for episode in range(100):
        r = 0
        for runn in range(100):
            r += play_q_learning(q)
        reward.append(r / 100)
    return reward


def play_q_learning(q, alpha=0.1):
    state = 3, 0
    terminal_state = 3, 11
    action = epsilon_greedy(q, state)
    total_reward = 0
    while state != terminal_state:
        next_state, reward = move(state, action)
        total_reward += reward
        next_action = epsilon_greedy(q, next_state)
        a, b = state[0], state[1]
        c, d = next_state[0], next_state[1]
        q[a][b][action] = q[a][b][action] + alpha * (reward + max(q[c][d][0], q[c][d][1], q[c][d][2], q[c][d][3] ) - q[a][b][action])
        state = next_state
        action = next_action
    return total_reward


def main():
    r1 = sarsa()
    r2 = q_learning()
    plt.plot(r1, 'b', r2, 'r')
    plt.savefig("sarsa vs q learning.png")


main()
