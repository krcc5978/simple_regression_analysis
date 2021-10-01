import numpy as np
import matplotlib.pyplot as plt

if __name__ == '__main__':
    data = np.loadtxt('sample_data.csv', delimiter=',', skiprows=1)
    speed = np.array(list(map(lambda x: x * 1.61, data[:, 1])))  # mph から km/h に変換
    dist = np.array(list(map(lambda y: y * 0.3048, data[:, 2])))  # ft から  m に変換

    fig = plt.figure(figsize=(10, 6))
    ax = fig.add_subplot(111)
    ax.set_title("Stopping Distances of Cars")
    ax.set_xlabel("speed(km/h)")
    ax.set_ylabel("distance(m)")
    plt.scatter(speed, dist)

    ave_speed = np.mean(speed)
    ave_dist = np.mean(dist)

    distributed_xx = np.sum(np.power(speed-ave_speed, 2))
    distributed_xy = np.sum((speed-ave_speed)*(dist-ave_dist))

    inclination = distributed_xy/distributed_xx
    intercept = ave_dist - inclination * ave_speed

    start = (0, intercept)
    end = 50, 50 * inclination + intercept

    x = np.linspace(0, 50, 50)
    y = 0.746606334842 * x - 5.41583710407
    plt.plot(x, y)
    plt.show()