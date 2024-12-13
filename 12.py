# pip install matplotlib
import matplotlib.pyplot as plt

def draw_circle(radius, center=(0, 0), color='green'):
    fig, ax = plt.subplots()
    circle = plt.Circle(center, radius, color=color, fill=True)
    ax.add_patch(circle)
    ax.set_xlim(center[0] - radius - 10, center[0] + radius + 10)
    ax.set_ylim(center[1] - radius - 10, center[1] + radius + 10)
    ax.set_aspect('equal', adjustable='box')
    plt.title(f'Circle: Radius {radius}, Center {center}, Color: {color}')
    plt.grid(True)
    plt.show()