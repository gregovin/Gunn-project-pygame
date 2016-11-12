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
        	 check(icon_path, image)
check(icon_path, "icon")
icon = pygame.image.load(icon_path)
import time
import math
import random
Enimils = []
def atan3(y, x):
   if x==0 and y==0:
      return 0
   elif x==0 and y>0:
      return math.pi/2
   elif x==0:
      return -math.pi/2
   else:
      return math.atan2(y, x)
class Enimy:
   def track(self, x, y):
     distx = x-self.pos[0]
     disty = y-self.pos[1]
     self.rot = atan3(disty,distx)
     self.vel[0] = 10 * math.cos(self.rot)
     self.vel[1] = 10 * math.sin(self.rot)
   def update(self):
      self.pos[0] = self.pos[0] + self.vel[0]
      self.pos[1] = self.pos[1] + self.vel[1]
      self.rot = atan3(self.vel[1], self.vel[0])
      
   def __init__(self, poses):
      self.pos = poses
      self.vel = [0, 0]
      self.rot = 0
class Lazer:
   def __init__ (self, positon, rotation):
      self.pos = positon
      self.rot = rotation
   def update(self):
      self.pos[0] += 5 * math.sin(self.rot)
      self.pos[1] += 5 * math.cos(self.rot)
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 155, 0)

display_width = 800
display_height = 600

gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Spaceships')
pygame.display.set_icon(icon)
Enimage = pygame.image.load('/Users/'+folder+'/Gunn-project-pygame-master/Enimy.png')
You = pygame.image.load('/Users/'+folder+'/Gunn-project-pygame-master/you.png')
lz = pygame.image.load('/users/'+folder+'/Gunn-project-pygame-master/lazer.png')
lz = pygame.transform.scale(lz, (100, lz.get_rect().height))
You = pygame.transform.rotate(You, -135)
You = pygame.transform.scale(You, (You.get_rect().width/5, You.get_rect().height/5))
clock = pygame.time.Clock()
Enimyrange=10
block_size = 20
FPS = 15
player = [display_width/2, display_height/2, 0, 0, 0]
direction = "right"
pygame.init()
smallfont = pygame.font.SysFont("comicsansms", 25)
medfont = pygame.font.SysFont("comicsansms", 50)
largefont = pygame.font.SysFont("comicsansms", 80)
pygame.key.set_repeat(100, 100)
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
            pygame.display.flip()
def score(score):
    text = smallfont.render("Score:" + str(score), True, black)
    gameDisplay.blit(text, [0,0])
print "init"
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
        message_to_screen("The objective of the game is to survive as long as posible", black, -30)
        message_to_screen("have fun", black, 10)
        message_to_screen("Press C to play, Q to quit, and P to pause.", black, 180)

        pygame.display.flip()
        clock.tick(15)


def display(Player):
    Disp = pygame.transform.rotate(You, -Player[4]*180/math.pi)
    gameDisplay.blit(Disp, (Player[0], Player[1]))
    Player[0] += Player[2]
    Player[1] += Player[4]

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

thyme = time.time()
lzls =[]
def gameLoop():
    gameExit = False
    gameOver = False

    lead_x = display_width / 2
    lead_y = display_height / 2

    lead_x_change = 10
    lead_y_change = 0

    Enimils = []
    lzls = []
    Player = [display_width/2, display_height/2, 0, 0, 0]
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
            pygame.display.flip()

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
                         Enimils = []
                         gameLoop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    Player[2] -= 1
                    lead_x_change = -block_size
                    lead_y_change = 0
                elif event.key == pygame.K_RIGHT:
                    Player[2] += 1
                    lead_x_change = block_size
                    lead_y_change = 0
                elif event.key == pygame.K_UP:
                    Player[3] -= 1
                    lead_y_change = -block_size
                    lead_x_change = 0
                elif event.key == pygame.K_DOWN:
                    Player[3] += 1
                    lead_y_change = block_size
                    lead_x_change = 0
                elif event.key == pygame.K_SPACE:
                    lzls.append(Lazer([player[0]+5*math.sin(player[4]),player[1]+5*math.cos(player[4])],player[4]))
                elif event.key == pygame.K_p:
                    pause()
        if Player[0] > display_width:
            Player[0] = 1
        elif player[0] < 0:
            Player[0] = display_width-1
        if Player[1] > display_height:
            Player[1] = 1
        elif Player[1] < 0:
            Player[1] = display_height-1
        Player[4] = atan3(Player[3], Player[2])
        gameDisplay.fill(white)
        #pygame.draw.rect(gameDisplay, red, [randAppleX, randAppleY, AppleThickness, AppleThickness])
        for i in Enimils:
            gameDisplay.blit(pygame.transform.rotate(Enimage, i.rot*180/math.pi), (i.pos[0], i.pos[1]))
            if (i.pos[0]-Player[0])**2 + (i.pos[1]-Player[1])**2 < Enimyrange ** 2:
                gameOver = True
            i.update()
            i.track(player[0], player[1])
        k = 0
        while k<len(lzls):
          v = 0
          gameDisplay.blit(pygame.transform.rotate(lz, lzls[k].rot * 180/math.pi), (lzls[k].pos[0], lzls[k].pos[1]))
          while v<len(Enimils):
               try:
                    if (lzls[k].pos[0] - Enimils[v].pos[0])**2 + (lzls[k].pos[1] - Enimils[v].pos[1])**2 < Enimyrange**2:
                         del lzls[k]
                         del Enimils[v]
                         v -= 1
                         k -= 1
               except:
                   v = 10000
               v += 1
          try:
               if lzls[k].pos[0] > display_width or lzls[k].pos[0] < 0:
                    del lzls[k]
                    k -= 1
               elif lzls[k].pos[1] > display_height or lzls[k].pos[1] < 0:
                    del lzls[k]
                    k -=1
               lzls[k].update()
               k += 1
          except:
               k = 10000
        display(Player)
        score(Player[4])
        pygame.display.flip()

        ##        if lead_x >= randAppleX and lead_x <= randAppleX + AppleThickness:
        ##            if lead_y >= randAppleY and lead_y <= randAppleY + AppleThickness:
        ##                randAppleX = round(random.randrange(0, display_width-block_size))#/10.0)*10.0
        ##                randAppleY = round(random.randrange(0, display_height-block_size))#/10.0)*10.0
        ##                snakeLength += 1

        if random.randint(0, 30) > 28:
            x, y = random.randint(0, display_width), random.randint(0, display_height)
            if (x-player[0])**2 + (y-player[1])**2 >= Enimyrange**2:
               Enimils.append(Enimy([x, y]))

        clock.tick(FPS)

    pygame.quit()
    quit()
print "intro"
game_intro()
print "loop"
gameLoop()
