import numpy as np
import matplotlib.pyplot as plt

plt.ion()  # Enable interactive mode
plt.style.use('dark_background')
fig, ax = plt.subplots()

plt.title("Levy Curve")

x_data = []
y_data = []

# Define transformation matrices
A = np.array([[0.5, 0.5], [-0.5, 0.5]])
B = np.array([[0.5, -0.5], [0.5, 0.5]])
c = np.array([[0.5], [0.5]])

# Initialize an empty plot
scat = ax.scatter([], [], s=1)
ax.set_xlim(-1.5, 0.5)
ax.set_ylim(-1.5, 0.5)


def random_transform(limit=25000, p=np.array([[0], [0]])):
    for i in range(limit):
        q = np.dot(B, p) - c
        p = np.dot(A, p)

        # Randomly swap p and q
        if np.random.rand() > 0.5:
            p, q = q, p

        x_data.append(p[0])
        y_data.append(p[1])
        x_data.append(q[0])
        y_data.append(q[1])

        scat.set_offsets(np.c_[x_data, y_data])
        plt.pause(0.0001)

    plt.ioff()
    plt.show()


if __name__ == "__main__":
    random_transform()
