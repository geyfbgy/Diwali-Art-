import turtle
import random
import time
import math
import threading

# Optional sound effects
try:
    import pygame
    pygame.mixer.init()
    firework_sound = pygame.mixer.Sound("firework.wav")  # Add your own sound file
except:
    pygame = None

# Setup screen
screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Happy Diwali Turtle Animation")
screen.setup(width=800, height=600)

t = turtle.Turtle()
t.hideturtle()
t.speed(0)
turtle.tracer(0, 0)

# Firework particle
class Particle:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.angle = random.uniform(0, 2*math.pi)
        self.speed = random.uniform(2,6)
        self.color = random.choice(["red", "yellow", "blue", "purple", "orange", "white"])
        self.size = random.randint(2,4)
        self.life = random.randint(20,50)
    
    def move(self):
        self.x += math.cos(self.angle) * self.speed
        self.y += math.sin(self.angle) * self.speed
        self.life -= 1

fireworks = []

def create_firework(x, y):
    if pygame:
        threading.Thread(target=lambda: firework_sound.play()).start()
    for _ in range(30):
        fireworks.append(Particle(x, y))

# Draw a diya with realistic flickering flame
def draw_diya(x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.fillcolor("gold")
    t.begin_fill()
    t.circle(20, 180)
    t.left(90)
    t.forward(40)
    t.left(90)
    t.circle(20, 180)
    t.left(90)
    t.forward(40)
    t.end_fill()
    
    # Flickering flame
    flame_colors = ["orange", "red", "yellow"]
    t.penup()
    t.goto(x, y+40)
    t.pendown()
    t.fillcolor(random.choice(flame_colors))
    t.begin_fill()
    size = random.randint(8,12)
    height = random.randint(18,22)
    t.circle(size, 180)
    t.left(90)
    t.forward(height)
    t.left(90)
    t.circle(size, 180)
    t.left(90)
    t.forward(height)
    t.end_fill()

# Floating lanterns
lanterns = []
for _ in range(25):
    lanterns.append([random.randint(-350, 350), random.randint(-250, -100), random.uniform(0.5, 2)])

# Main animation loop
while True:
    t.clear()
    
    # Draw diyas
    for x in range(-300, 301, 150):
        draw_diya(x, -200)
    
    # Random fireworks
    if random.randint(0, 20) == 0:  # Random chance each frame
        create_firework(random.randint(-300, 300), random.randint(0, 200))
    
    # Draw fireworks
    for p in fireworks[:]:
        t.penup()
        t.goto(p.x, p.y)
        t.pendown()
        t.dot(p.size*3, p.color)
        p.move()
        if p.life <= 0:
            fireworks.remove(p)
    
    # Draw lanterns
    t.penup()
    for l in lanterns:
        t.goto(l[0], l[1])
        t.dot(8, "yellow")
        l[1] += l[2]
        l[0] += random.uniform(-0.5, 0.5)
        if l[1] > 300:
            l[1] = -250
            l[0] = random.randint(-350, 350)
    
    # Glowing Happy Diwali text
    t.penup()
    t.goto(0, 150)
    glow_colors = ["red", "yellow", "orange", "white"]
    t.color(random.choice(glow_colors))
    t.write("🎉 Happy Diwali 🎉", align="center", font=("Arial", 36, "bold"))
    
    turtle.update()
    time.sleep(0.05)
