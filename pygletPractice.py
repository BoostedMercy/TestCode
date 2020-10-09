import pyglet
import random as r
import requests


def GenerateStuffs(h, w):
    s, c = r.randint(1, 20), r.randint(1, 10)
    shapeList = []
    for square in range(s):
        shapeList.append(pyglet.shapes.Rectangle(r.randint(0, h), r.randint(0, w), r.randint(100, 300), r.randint(100, 300), color=(r.randint(1, 255), r.randint(1, 255), r.randint(1, 255))))
        shapeList[-1].opacity, shapeList[-1].rotation = r.randint(100, 255), r.randint(0,360)
    return shapeList


a = requests.get("https://raw.githubusercontent.com/dwyl/english-words/master/words_dictionary.json")
words = a.json()


window = pyglet.window.Window(1280, 720, caption="Testing", resizable=True)
label = pyglet.text.Label("This is normal, for now...", font_name="Comic Sans MS", font_size=72, x=window.width // 2, y=window.height // 2,
                          anchor_x='center', anchor_y='center')
shape = pyglet.shapes.Rectangle(0, 0, 1280, 720, color=(0, 0, 0))


@window.event
def on_draw():
    window.clear()
    shape.draw()
    h, w = window.get_size()
    shapeList = GenerateStuffs(h, w)
    for s in shapeList:
        s.draw()

    label.draw()


@window.event
def on_resize(width, height):
    x, y = window.get_location()
    print(f"the new res {width, height}")
    window.clear()
    window.set_location(x + r.randint(5, 20), y + r.randint(5,20))
    shape.width, shape.height, shape.color = width, height, (r.randint(1, 255), r.randint(1, 255), r.randint(1, 255))
    label.x, label.y, label.text = width//2, height//2, r.choice(list(words.keys()))
    label.color = (r.randint(1, 255), r.randint(1, 255), r.randint(1, 255), 255)
    shapeList = GenerateStuffs(height, width)
    shape.draw()
    for s in shapeList:
        s.draw()
    label.draw()


pyglet.app.run()
