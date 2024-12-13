# pip install matplotlib
import ssl
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from urllib.request import urlopen
from io import BytesIO


def display_image_on_canvas(image_url, canvas_width, canvas_height, position, size):
    ssl._create_default_https_context = ssl._create_unverified_context
    fig, ax = plt.subplots(figsize=(canvas_width / 100, canvas_height / 100))

    with urlopen(image_url) as response:
        image_data = BytesIO(response.read())
    img = mpimg.imread(image_data, format='jpeg')

    x, y = position
    img_width, img_height = size
    ax.imshow(img, extent=(x, x + img_width, y, y + img_height))

    ax.set_xlim(0, canvas_width)
    ax.set_ylim(0, canvas_height)
    ax.set_aspect('equal')
    # ax.axis('off')
    plt.grid(False)
    plt.show()

display_image_on_canvas(
"https://picsum.photos/536/354",
   800, 600, (100, 100), (300, 200)
)