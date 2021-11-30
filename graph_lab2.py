from PIL import Image, ImageColor, ImageDraw
import pandas as pd

width = 960
height = 540
image = Image.new("RGB", (width, height), (255, 255, 255))
filepath = input("Введіть шлях до файлу: ")
df = pd.read_csv(filepath, sep=" ", header=None)
h = ['x', 'y']
df.columns = h

drawing = ImageDraw.Draw(image)
for index, row in df.iterrows():
    x, y = row['y'], 540 - row['x']
    drawing.point((x, y), fill=ImageColor.getrgb("red"))
image.show()
name = input("Введіть назву для збереженої картинки(у вигляді 'file_name.png'):")
image.save(name, "PNG")