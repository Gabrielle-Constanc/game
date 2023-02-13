WIDTH = 400
HEIGHT = 400
score = 0
game_over = False
ant= Actor("ant.png")
ant.pos = 100, 100
leaf = Actor("leaf.png")
leaf.pos = 200, 200

def draw():
    screen.fill("green")
    ant.draw()
    leaf.draw()
    screen
