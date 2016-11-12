folder = str(input("what is the folder path of the downloaded folder?"))
folder = folder.replace("/?Users/", "")
folder = folder.replace("C:/", "")
folder = folder.replace("/?Gunn-project-pygame/?", "")
folder = folder.replace("/\z", "")
icon_path = "/Users/" + folder + "/Gunn-project-pygame-master/spaceship.jpeg"
import pygame
def check(path,image):
     print path
     try:
     	icon = pygame.image.load(path)
     except:
     	print("remember to include you username!")
     	folder = str(input("Not a valid forlder path, what is the folder path of the downloaded folder?"))
     	if image == "icon":
        	 pt2 = "/Gunn-project-pygame/spaceship.jpeg"
        	 folder = folder.replace("C:/Users/", "")
         	 folder = folder.replace("/?Gunn-project-pygame/?", "")
        	 folder = folder.replace("/\z", "")
        	 icon_path = "C:/Users/" + folder + pt2
        	 icon_check(icon_path, image)
check(icon_path, "icon")
icon = pygame.image.load(icon_path)
import time
import random
def atan3(y, x):
   if x==0 and y==0:
      return 0
   elif x==0 and y>0:
      return math.pi/2
   elif x==0:
      return -math.pi/2
   else:
      return math.atan2(y, x)
player = [200, 200, 0, 0, 0]
class Enimy:
   def update(self):
      self.pos[0] = self.pos[0] + self.vel[0]
      self.pos[1] = self.pos[1] + self.vel[1]
      self.rot = atan3(vel[1]/vel[0])
      
   def __init__(self, poses, vels):
      self.pos = poses
      self.vel = vels
      self.rot = atan3(vels[1],vels[0])
class Lazer:
   def __init__ (positon, rotation):
      pos = position
      rot = rotation
   def update(self):
      self.pos[0] += 10 * math.sin(rotation)
      self.pos[1] += 10 * math.cos(rotation)
pygame.init()

white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 155, 0)

display_width = 800
display_height = 600

gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Spaceships')
pygame.display.set_icon(icon)
Enimy = pygame.image.load('/Users/'+folder+'/Enimy.png')
You = pygame.image.load('/User/'+folder+'/you.png')

clock = pygame.time.Clock()
AppleThickness = 30
block_size = 20
FPS = 15
direction = "right"

smallfont = pygame.font.SysFont("comicsansms", 25)
medfont = pygame.font.SysFont("comicsansms", 50)
largefont = pygame.font.SysFont("comicsansms", 80)
def pause():
    paused = True
    while paused:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    paused = False
                elif event.key == pygame.K_q:
                  pygame.quit()
                  quit()
            #gameDisplay.fill(white)
            message_to_screen("Paused", black, -100, size = "large")
            message_to_screen("Press C to continue or Q to quit.", black, 25)
            pygame.display.update()
def score(score):
    text = smallfont.render("Score:" + str(score), True, black)
    gameDisplay.blit(text, [0,0])
def randAppleGen():
    randAppleX = round(random.randrange(0, display_width - AppleThickness))  # /10.0)*10.0
    randAppleY = round(random.randrange(0, display_height - AppleThickness))  # /10.0)*10.0
    return randAppleX, randAppleY

def game_intro():
    intro = True
    while intro:
        for event in pygame.event.get():
            if event.type ==pygame.QUIT:
                pygame.quit()
                quit()
            if event.type ==pygame.KEYDOWN:
                if event.key ==pygame.K_c:
                    intro = False #make the intro thing gone, and end the loop.
                if event.key ==pygame.K_q:
                    pygame.quit()
                    quit()

        gameDisplay.fill(white)
        message_to_screen("Welcome to Spaceships", green, -100, size = "large")
        message_to_screen("The objective of the game is to eat red apples", black, -30)
        message_to_screen("The more apples you eat the longer you become.", black, 10)
        message_to_screen("If you run into yourself, or the edges, you lose", black, 50)
        message_to_screen("Press C to play, Q to quit, and P to pause.", black, 180)

        pygame.display.update()
        clock.tick(15)


def snake(block_size, snakelist):
    if direction == "right":
        head = pygame.transform.rotate(img, 270)

    if direction == "left":
        head = pygame.transform.rotate(img, 90)

    if direction == "up":
        head = img

    if direction == "down":
        head = pygame.transform.rotate(img, 180)

    gameDisplay.blit(head, (snakelist[-1][0], snakelist[-1][1]))

    for XnY in snakelist[:-1]:
        pygame.draw.rect(gameDisplay, green, [XnY[0], XnY[1], block_size, block_size])


def text_objects(text, color, size):
    if size == "small":
        textSurface = smallfont.render(text, True, color)
    elif size == "medium":
        textSurface = medfont.render(text, True, color)
    elif size == "large":
        textSurface = largefont.render(text, True, color)

    return textSurface, textSurface.get_rect()


def message_to_screen(msg, color, y_displace=0, size="small"):
    textSurf, textRect = text_objects(msg, color, size)
    textRect.center = (display_width / 2), (display_height / 2) + y_displace
    gameDisplay.blit(textSurf, textRect)


def gameLoop():
    global direction
    gameExit = False
    gameOver = False
    direction = "right"

    lead_x = display_width / 2
    lead_y = display_height / 2

    lead_x_change = 10
    lead_y_change = 0

    snakeList = []
    snakeLength = 1

    randAppleX = round(random.randrange(0, display_width - AppleThickness))  # /10.0)*10.0
    randAppleY = round(random.randrange(0, display_height - AppleThickness))  # /10.0)*10.0

    while not gameExit:
        if gameOver:
            gameDisplay.fill(white)
            message_to_screen("Game over",
                              red,
                              y_displace=-50,
                              size="large")

            message_to_screen("Press C to play again or Q to quit",
                              black,
                              50,
                              size="medium")
            pygame.display.update()

        while gameOver :
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    gameOver = False
                    gameExit = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        gameExit = True
                        gameOver = False
                    if event.key == pygame.K_c:
                        gameLoop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    direction = "left"
                    lead_x_change = -block_size
                    lead_y_change = 0
                elif event.key == pygame.K_RIGHT:
                    direction = "right"
                    lead_x_change = block_size
                    lead_y_change = 0
                elif event.key == pygame.K_UP:
                    direction = "up"
                    lead_y_change = -block_size
                    lead_x_change = 0
                elif event.key == pygame.K_DOWN:
                    direction = "down"
                    lead_y_change = block_size
                    lead_x_change = 0
                elif event.key == pygame.K_p:
                    pause()

        if lead_x >= display_width or lead_x < 0 or lead_y >= display_height or lead_y < 0:
            gameOver = True

        lead_x += lead_x_change
        lead_y += lead_y_change

        gameDisplay.fill(white)


        #pygame.draw.rect(gameDisplay, red, [randAppleX, randAppleY, AppleThickness, AppleThickness])
        gameDisplay.blit(apple_img, (randAppleX, randAppleY))
        snakeHead = []
        snakeHead.append(lead_x)
        snakeHead.append(lead_y)
        snakeList.append(snakeHead)

        if len(snakeList) > snakeLength:
            del snakeList[0]

        for eachSegment in snakeList[:-1]:
            if eachSegment == snakeHead:
                gameOver = True

        snake(block_size, snakeList)
        score(snakeLength-1)
        pygame.display.update()

        ##        if lead_x >= randAppleX and lead_x <= randAppleX + AppleThickness:
        ##            if lead_y >= randAppleY and lead_y <= randAppleY + AppleThickness:
        ##                randAppleX = round(random.randrange(0, display_width-block_size))#/10.0)*10.0
        ##                randAppleY = round(random.randrange(0, display_height-block_size))#/10.0)*10.0
        ##                snakeLength += 1

        if lead_x > randAppleX and lead_x < randAppleX + AppleThickness or lead_x + block_size > randAppleX and lead_x + block_size < randAppleX + AppleThickness:

            if lead_y > randAppleY and lead_y < randAppleY + AppleThickness:

                randAppleX, randAppleY = randAppleGen()
                snakeLength += 1

            elif lead_y + block_size > randAppleY and lead_y + block_size < randAppleY + AppleThickness:

                randAppleX, randAppleY = randAppleGen()
                snakeLength += 1

        clock.tick(FPS)

    pygame.quit()
    quit()
game_intro()

gameLoop()
