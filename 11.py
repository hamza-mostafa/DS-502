####################
## USING Terminal ##
####################

# pip install colorama
from colorama import Fore, Style

def draw_rectangle(width, height, color="green"):
    color = getattr(Fore, color.upper(), Fore.WHITE)
    for _ in range(height):
        print(color + Style.BRIGHT, f"{'#' * width}{Style.RESET_ALL}")


######################
## USING MATPLOTLIB ##
######################

# pip install matplotlib
import matplotlib.pyplot as plt

def draw_rectangle2(width, height, color='blue', x=0, y=0):
    fig, ax = plt.subplots()
    rectangle = plt.Rectangle((x, y), width, height, color=color)
    ax.add_patch(rectangle)
    ax.set_xlim(-10, max(width + x + 10, 10))
    ax.set_ylim(-10, max(height + y + 10, 10))
    ax.set_aspect('equal', adjustable='box')
    plt.title(f'Rectangle: {width}x{height}, Color: {color}')
    plt.grid(True)
    plt.show()
