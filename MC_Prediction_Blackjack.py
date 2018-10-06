import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt

def play():
    p1, p2 = hit(), hit()
    if p1 == 1:
        p1 = 11
    if p2 == 1:
        p2 = 11
    d1_visible, d2 = hit(), hit()
    state_list = []  # (usable ace, player sum, dealer showing )
    usable_ace = p1 == 11 or p2 == 11

    # Player Plays
    sum = p1 + p2
    if sum > 21:
        return -1, state_list

    while get_move(sum) == 'hit':
        if sum >= 12:
            state_list.append((usable_ace, sum-12, d1_visible-1))
        temp = hit()
        sum += temp
        if temp == 1 and sum < 12:
            usable_ace = True
            sum += 10
    if sum <= 21:
        state_list.append((usable_ace, sum - 12, d1_visible - 1))

    # Dealer Plays
    d_sum = dealer_play(d1_visible, d2)

    if sum > 21:
        # ("Player Bust")
        return -1, state_list
    elif sum == d_sum:
        return 0, state_list
    elif d_sum > 21:
        # ("Dealer bust")
        return 1, state_list
    else:
        return -1, state_list


def hit():
    a = [i for i in range(1, 11)]
    for i in range(3):
        a.append(10)
    return np.random.choice(a)


def get_move(sum):
    if sum < 20:
        return 'hit'
    else:
        return 'stick'


# a,b are the initial card values of the dealer
def dealer_play(a, b):
    sum = a + b
    while (sum < 17):
        temp = hit()
        sum += temp
    return sum


def main():
    v = [
        [[ 0 for j in range(10)] for i in range(10)],
        [[ 0 for j in range(10)] for i in range(10)]
    ]
    count = [
        [[ 0 for j in range(10)] for i in range(10)],
        [[ 0 for j in range(10)] for i in range(10)]
    ]
    for episode in range(5000000):
        if episode % 100 == 0:
            print("Running episode ", episode)
        reward, state_list = play()
        g = reward
        for step in reversed(state_list):
            # print(step)
            count[step[0]][step[1]][step[2]] += 1
            v[step[0]][step[1]][step[2]] = incremental(v[step[0]][step[1]][step[2]], g, count[step[0]][step[1]][step[2]])

    for i in v[0]:
        print(i)
    #plotting the results
    # fig = plt.figure()
    # ax = fig.add_subplot(111, projection='3d')
    # ax.plot_surface(x = , y = , z, color='b')
    # a = [1 for i in range]

    plt.show()


def incremental(old, val, n):
    new = (old + (1.0 / n) * (val - old))
    return new


main()
