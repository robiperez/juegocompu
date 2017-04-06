import pyglet 

altura = 15
v = 1

game_window = pyglet.window.Window(600, 400)

background = pyglet.image.load_animation('background.gif')
back = pyglet.sprite.Sprite(background)

caraimg = pyglet.image.load_animation('cara.gif')
cara = pyglet.sprite.Sprite(caraimg, x = 5, y = altura)

boximg = pyglet.image.load('caja.png')
box = pyglet.sprite.Sprite(boximg, x=600, y = 5)
box2 = pyglet.sprite.Sprite(boximg, x=1000, y = 5)
box3 = pyglet.sprite.Sprite(boximg, x=1400, y = 5)
box4 = pyglet.sprite.Sprite(boximg, x=1800, y = 5)
box5 = pyglet.sprite.Sprite(boximg, x=2200, y = 5)
box6 = pyglet.sprite.Sprite(boximg, x=2600, y = 5)
box7 = pyglet.sprite.Sprite(boximg, x=3000, y = 5)
box8 = pyglet.sprite.Sprite(boximg, x=3400, y = 5)
box9 = pyglet.sprite.Sprite(boximg, x=3800, y = 5)
box10 = pyglet.sprite.Sprite(boximg, x=4200, y = 5)
box11 = pyglet.sprite.Sprite(boximg, x=4600, y = 5)
box12 = pyglet.sprite.Sprite(boximg, x=5000, y = 5)
box13 = pyglet.sprite.Sprite(boximg, x=5400, y = 5)
box14 = pyglet.sprite.Sprite(boximg, x=5800, y = 5)
box15 = pyglet.sprite.Sprite(boximg, x=6200, y = 5)
box16 = pyglet.sprite.Sprite(boximg, x=6600, y = 5)
box17 = pyglet.sprite.Sprite(boximg, x=7000, y = 5)
box18 = pyglet.sprite.Sprite(boximg, x=7400, y = 5)
box19 = pyglet.sprite.Sprite(boximg, x=7800, y = 5)
box20 = pyglet.sprite.Sprite(boximg, x=8200, y = 5)
box21 = pyglet.sprite.Sprite(boximg, x=8600, y = 5)
box22 = pyglet.sprite.Sprite(boximg, x=9000, y = 5)
box23 = pyglet.sprite.Sprite(boximg, x=9400, y = 5)
box24 = pyglet.sprite.Sprite(boximg, x=9800, y = 5)
box25 = pyglet.sprite.Sprite(boximg, x=10200, y = 5)
box26 = pyglet.sprite.Sprite(boximg, x=10600, y = 5)
box27 = pyglet.sprite.Sprite(boximg, x=10200, y = 5)
box28 = pyglet.sprite.Sprite(boximg, x=10600, y = 5)

snd = pyglet.media.load('Shooting_01.wav')
looper = pyglet.media.SourceGroup(snd.audio_format, None)
looper.loop = True
looper.queue(snd)
p = pyglet.media.Player()
p.queue(looper)
p.play()

@game_window.event
def on_draw():
	game_window.clear()
	back.draw()
	box.draw()
	box2.draw()
	box3.draw()
	box4.draw()
	box5.draw()
	box6.draw()
	box7.draw()
	box8.draw()
	box9.draw()
	box10.draw()
	box11.draw()
	box12.draw()
	box13.draw()
	box13.draw()
	box14.draw()
	box15.draw()
	box16.draw()
	box17.draw()
	box18.draw()
	box19.draw()
	box20.draw()
	box21.draw()
	box22.draw()
	box23.draw()
	box24.draw()
	box25.draw()
	box26.draw()
	box27.draw()
	box28.draw()
	cara.draw()

from pyglet.window import key

@game_window.event
def update(dt):
    box.x += dt * -200
    box2.x += dt * -200
    box3.x += dt * -200
    box4.x += dt * -200
    box5.x += dt * -200
    box6.x += dt * -200
    box7.x += dt * -200
    box8.x += dt * -200
    box9.x += dt * -200
    box10.x += dt * -200
    box11.x += dt * -200
    box12.x += dt * -200
    box13.x += dt * -200
    box14.x += dt * -200
    box15.x += dt * -200
    box16.x += dt * -200
    box17.x += dt * -200
    box18.x += dt * -200
    box19.x += dt * -200
    box20.x += dt * -200
    box21.x += dt * -200
    box22.x += dt * -200
    box23.x += dt * -200
    box24.x += dt * -200
    box25.x += dt * -200
    box26.x += dt * -200
    box27.x += dt * -200
    box28.x += dt * -200
    if v == 0:
    	altura += 2

@game_window.event
def on_key_press(symbol, modifier):
    global altura
    if symbol == key.A:
    	v = 0

if box.x == -1:
    	box = pyglet.sprite.Sprite(boximg, x=600, y = 5)

pyglet.clock.schedule_interval(update, 1/60.)

pyglet.app.run()
