import pyglet 
import time

game_window = pyglet.window.Window(600, 400)

background = pyglet.image.load_animation('background.gif')
back = pyglet.sprite.Sprite(background)

caraimg = pyglet.image.load_animation('cara.gif')
cara = pyglet.sprite.Sprite(caraimg, x = 5, y = 15)


boximg = pyglet.image.load('caja.png')
box = pyglet.sprite.Sprite(boximg, x=600, y = 5)


#music = pyglet.media.load('Bounce.wav')
#music.play()

start_time = time.time()
elapsed_time = time.time() - start_time

label = pyglet.text.Label(elapsed_time,)

@game_window.event
def on_draw():
	game_window.clear()
	back.draw()
	box.draw()
	cara.draw()
	label.draw()

def on_mouse_press():
	box.draw()


def update(dt):
    
    box.x += dt * -100


pyglet.clock.schedule_interval(update, 1/60.)

pyglet.app.run()
