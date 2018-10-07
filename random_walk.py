import numpy as np


def play(state):
    options = [state + 1, state - 1]
    s = np.random.choice(options)
    reward = 0
    if s == 6:
        reward = 1
    # print(s, reward)
    return s, reward


def td(alpha = 0.1):
    v = np.zeros(7)
    for i in range(1,6):
        v[i] = 0.5
    terminal_state = [0, 6]
    observe = [1, 10, 100, 1000]
    for episode in range(101):
        state = 3
        while state not in terminal_state:
            state_new, reward = play(state)
            v[state] = v[state] + alpha* (reward + v[state_new] - v[state])
            state = state_new
        if episode in observe:
            for i in range(1, 6):
                print (v[i], ",", end = "")
            print()

td()
