import pystray
from PIL import Image, ImageDraw
import sys

def create_image():
    # Create an image with a simple drawing
    width = 64
    height = 64
    image = Image.new('RGB', (width, height), (255, 255, 255))
    dc = ImageDraw.Draw(image)
    dc.rectangle(
        (width // 2 - 10, height // 2 - 10, width // 2 + 10, height // 2 + 10),
        fill=(0, 0, 0))
    return image

def on_quit(icon, item):
    icon.stop()
    sys.exit()

def setup(icon):
    icon.visible = True

icon = pystray.Icon("test_icon")
icon.icon = create_image()
icon.menu = pystray.Menu(
    pystray.MenuItem("Quit", on_quit)
)
icon.run(setup)
