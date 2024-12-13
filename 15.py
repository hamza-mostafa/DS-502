# pip install matplotlib
from typing import Tuple, TypedDict
import matplotlib.pyplot as plt

class TextProperties(TypedDict):
    message: str
    size: int
    color: str
    position: Tuple[int, int]

def display_text_on_canvas(
    canvas_width: int,
    canvas_height: int,
    bg_color: str,
    text: TextProperties
):
    fig, ax = plt.subplots(figsize=(canvas_width / 100, canvas_height / 100))

    fig.patch.set_facecolor(bg_color)
    ax.set_facecolor(bg_color)

    ax.text(
        text['position'][0],
        text['position'][1],
        text['message'],
        color=text['color'],
        fontsize=text['size'],
        ha='center',
        va='center'
    )

    ax.set_xlim(0, canvas_width)
    ax.set_ylim(0, canvas_height)
    # ax.axis('off')
    plt.grid(False)

    plt.show()

display_text_on_canvas(
    800,
    400,
    'lightblue',
    {
        'message': "Hello!",
        'size': 20,
        'color': 'red',
        'position': (400, 200)
    }
)