# pip install matplotlib
import matplotlib.pyplot as plt

def draw_line(start_point, end_point, thickness, color):
    fig, ax = plt.subplots()
    ax.plot(
        [start_point[0], end_point[0]], [start_point[1], end_point[1]],
        linewidth=thickness,
        color=color
    )
    ax.set_xlim(min(start_point[0], end_point[0]) - 10, max(start_point[0], end_point[0]) + 10)
    ax.set_ylim(min(start_point[1], end_point[1]) - 10, max(start_point[1], end_point[1]) + 10)
    ax.set_aspect('equal', adjustable='box')
    plt.title(f'Line: Start {start_point}, End {end_point}, Thickness {thickness}, Color {color}')
    plt.grid(True)
    plt.show()

draw_line((-5, 5), (15, -10), 2, 'black')