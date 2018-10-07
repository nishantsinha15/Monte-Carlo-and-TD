import numpy as np
import matplotlib.pyplot as plt


def play(state):
    options = [state + 1, state - 1]
    s = np.random.choice(options)
    reward = 0
    if s == 6:
        reward = 1
    # print(s, reward)
    return s, reward


def mc(alpha = 0.01):
    v = np.zeros(7)
    v_true = [0]
    error = []
    temp = 1
    for i in range(1,6):
        v[i] = 0.5
        v_true.append(temp/6)
        temp += 1
    terminal_state = [0, 6]
    for episode in range(100):
        reward = 0
        state = 3
        state_list = [state]
        while state not in terminal_state:
            state_new, reward = play(state)
            state_list.append(state_new)
            state = state_new
        g = reward
        e = 0
        for state in reversed(state_list):
            if state not in terminal_state:
                v[state] = v[state] + alpha*(g - v[state])
                e += (v_true[state] - v[state]) ** 2
        error.append(np.math.sqrt(e / 5))
    # for e in error:
    #     print(e)
    return error

def td(alpha = 0.1):
    v = np.zeros(7)
    v_true = [0]
    error = []
    temp = 1
    for i in range(1,6):
        v[i] = 0.5
        v_true.append(temp/6)
        temp += 1
    terminal_state = [0, 6]
    for episode in range(100):
        state = 3
        while state not in terminal_state:
            state_new, reward = play(state)
            v[state] = v[state] + alpha* (reward + v[state_new] - v[state])
            state = state_new
        e = 0
        for i in range(1, 6):
            e += (v_true[i] - v[i])**2
        error.append(np.math.sqrt(e / 5))
    # for e in error:
    #     print(e)
    return error


def main():
    error1 = []
    for i in [0.15, 0.1, 0.05]:
        e = np.zeros(100)
        for run in range(100):
            e += td(i)
        e /= 100
        error1.append(e)
    error2 = []
    for i in [0.01, 0.02, 0.03, 0.04]:
        e = np.zeros(100)
        for run in range(100):
            e += mc(i)
        e /= 100
        error2.append(e)
    plt.plot(np.asarray(error1).T, 'b', np.asarray(error2).T, 'r')


    plt.savefig('randomwalk2.png')


# mc()
main()