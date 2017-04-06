import pyglet 

game_window = pyglet.window.Window(600, 400)

background = pyglet.image.load_animation('background.gif')
back = pyglet.sprite.Sprite(background)

#back.queue(background)

caraimg = pyglet.image.load_animation('cara.gif')
cara = pyglet.sprite.Sprite(caraimg, x = 5, y = 40)


#music = pyglet.media.load('Bounce.wav')
#music.play(-1,0.0)


@game_window.event
def on_draw():
	game_window.clear()
	back.draw()
	cara.draw()

#def on_

#def update(dt):
 


#pyglet.clock.schedule_interval(update, 1/60.)

pyglet.app.run()
