import os
import random
import time

#Import the Turtle module
import turtle
#Required by Mac os system to show the window.
turtle.fd(0)
#set the animations speed to the max speed there is.
turtle.speed(0)
#this below is the color of the background.
turtle.bgcolor("black")
turtle.title("MatthewB- Spacewar")
#Adding in the space background to this game
turtle.bgpic("starfield.gif")
#This hides the turtle
turtle.ht()
#This saves the memory
turtle.setundobuffer(1)
# this speeds up the drawing
turtle.tracer(0)

class Sprite(turtle.Turtle):
    def __init__(self,spriteshape, color, startx, starty):
        turtle.Turtle.__init__(self, shape = spriteshape)
        self.speed(0)
        self.penup()
        self.color(color)
        self.fd(0)
        self.goto(startx, starty)
        self.speed = 1

    def move(self): # this sets all "self spees to the below "
        self.fd(self.speed)

        # boundarys for the game are being set below.
        if self.xcor() > 290:
            self.setx(290) # This stops the triangle from flowing outside the lines
            self.rt(60)

        if self.xcor() < -290:
            self.setx (-290) # this stop ths player from going out of the line
            self.rt(60)

        if self.ycor() > 290:
            self.sety(290) # same here
            self.rt(60)

        if self.ycor() < -290:
            self.sety(-290) # same here
            self.rt(60)


    def is_collision(self, other): # This is the detection to allow  crash in game
        if (self.xcor() >= (other.xcor() - 20)) and \
           (self.xcor() <= (other.xcor() + 20)) and \
           (self.ycor() >= (other.ycor() - 20)) and \
           (self.ycor() <= (other.ycor() + 20)):
                return True
        else:
                return False


class Player(Sprite):

    def __init__(self,spriteshape, color, startx, starty):
        Sprite.__init__(self, spriteshape, color, startx, starty)
        self.shapesize(stretch_wid=0.4,stretch_len=1.5,outline= None)
        self.speed = 4
        self.lives = 3

    def turn_left(self):
        self.lt(45)

    def turn_right(self):
        self.rt(45) # this allows the correct button to be pressed on the keyboard.

    def accelerate(self):
        self.speed += 1

    def decelerate(self):
        self.speed -= 1


class Enemy(Sprite): # ENEMY

    def __init__(self,spriteshape, color, startx, starty):
        Sprite.__init__(self, spriteshape, color, startx, starty)
        self.speed = 6
        self.setheading(random.randint(0,360))



class Ally(Sprite): # Ally

    def __init__(self,spriteshape, color, startx, starty):
        Sprite.__init__(self, spriteshape, color, startx, starty)
        self.speed = 8
        self.setheading(random.randint(0,360))

    def move(self): # this sets all "self speed to the below "
        self.fd(self.speed)

        # boundarys for the game are being set below.
        if self.xcor() > 290:
            self.setx(290) # This stops the triangle from flowing outside the frame
            self.lt(60)

        if self.xcor() < -290:
            self.setx (-290) # this stops the  player from going out of the frame
            self.lt(60)

        if self.ycor() > 290:
            self.sety(290) # same here
            self.lt(60)

        if self.ycor() < -290:
            self.sety(-290) # same here
            self.lt(60)




class Missile(Sprite):
    def __init__(self,spriteshape, color, startx, starty):
        Sprite.__init__(self, spriteshape, color, startx, starty)
        self.shapesize(stretch_wid=0.3, stretch_len=0.4, outline=None)
        self.speed = 29
        self.status = "ready"
        self.goto(-1000, 1000) # This moves the missle off the screen.

    def fire(self):
        if self.status == "ready":
            self.goto(player.xcor(), player.ycor()) # This launches the missle off the white triangle where ever the triangle is
            self.setheading(player.heading())
            self.status = "firing"

    def move(self):
        if self.status == "ready":
            self.goto(-1000, 1000)  # This moves the missle off the screen.

        if self.status == "firing":
            self.fd(self.speed)
        #border check below

        if self.xcor() < -290 or self.xcor() >290 or \
           self.ycor() < - 290 or self.ycor() > 290:
           self.goto(-1000,1000)
           self.status = "ready"



class Particle(Sprite): #

    def __init__(self,spriteshape, color, startx, starty):
        Sprite.__init__(self, spriteshape, color, startx, starty)
        self.shapesize(stretch_wid=0.1, stretch_len=0.1, outline=None)
        self.goto(-1000,-1000)
        self.frame = 0

    def explode(self,startx, starty):
        self.goto(startx,starty)
        self.setheading(random.randint(0,360))
        self.frame =1

    def move(self):
        if self.frame > 0:
            self.fd(10)
            self.frame += 1

        if self.frame >12:
            self.frame = 0
            self.goto(-1000, -1000)

class Game():

    def __init__(self):
        self.level = 1
        self.score = 0
        self.state = "playing"
        self.pen = turtle.Turtle()
        self.lives = 3


    def draw_boarder(self):
        #drawing a board around the square boarder
        self.pen.speed(0)
        self.pen.color("white")
        self.pen.pensize(3)
        self.pen.penup()
        self.pen.goto(-300, 300)
        self.pen.down()
        for side in range (4):
            self.pen.fd(600)
            self.pen.rt(90)
        self.pen.penup()
        self.pen.ht()
        self.pen.pendown()

    def show_status(self):
        self.pen.undo()
        msg = "Score: %s" %(self.score)
        self.pen.penup()
        self.pen.goto(-300,310)
        self.pen.write(msg, font=("Arial", 16, "normal"))



# game object
game = Game()

#Drawing the border for the game
game.draw_boarder()



#show the game status inside the game
game.show_status()


#create my sprites
player = Player("triangle", "white", 0, 0)
#enemy = Enemy("circle", "red", -100, 0)
missile = Missile("triangle", "yellow", 0, 0)
#ally = Ally("square", "blue", 0,0)



enemies =[]
for i in range(6):
    enemies.append(Enemy("circle", "red", -100, 0))

allies =[]
for i in range(6):
    allies.append(Ally("square", "blue", 0,0))

particles = []
for i in range(20):
    particles.append(Particle("circle" , "orange", 0, 0))


#keyboard inputs (left right up and down )
turtle.onkey(player.turn_left,"Left")
turtle.onkey(player.turn_right,"Right")
turtle.onkey(player.accelerate,"Up")
turtle.onkey(player.decelerate,"Down")
turtle.onkey(missile.fire, "space")
turtle.listen()


#Main game Loop!!!!!!

while True:
    turtle.update()
    time.sleep(0.05)
    player.move()
    missile.move()


    for enemy in enemies:
        enemy.move()
        # check for a crash
        if player.is_collision(enemy):
            x = random.randint(-250, 250)
            y = random.randint(-250, 250)
            enemy.goto(x, y)
            game.score -= 100
            game.show_status()

        # check for a crash between the missile and the enemey
        if missile.is_collision(enemy):
            x = random.randint(-250, 250)
            y = random.randint(-250, 250)
            enemy.goto(x, y)
            missile.status = "ready"
            # increase the score to inside the game.
            game.score += 100
            game.show_status()
            for particle in particles :
                particle.explode(missile.xcor(),missile.ycor ())

    for ally in allies:
        ally.move()
        # check for a crash between the missile and the Ally

        if missile.is_collision(ally):
            x = random.randint(-250, 250)
            y = random.randint(-250, 250)
            ally.goto(x, y)
            missile.status = "ready"
            #Drecease the score if you shoot the ally
            game.score -= 50
            game.show_status()

    for particle in particles :
        particle.move()


delay = raw_input("Press enter to Finsish. > ")
