# Snake Game
# Import Statements
import pygame,time,random,sys

# Pygame initialisation
check_error=pygame.init()

#Checking For Errors
if(check_error[1]>0):
    print('Had Initialisation Errors exiting......')
    sys.exit(-1)
else:
    print('(+)Pygame Succesfully initialiZed!')
    
# Sound Variables
crash_sound=pygame.mixer.Sound("Collision.wav")
snakebit_sound=pygame.mixer.Sound('snakehiss2.wav')
gameover_sound=pygame.mixer.Sound('gameover.wav')
pygame.mixer.music.load('Snack_Time.mp3')

#Background music
pygame.mixer.music.play(-1)

# Game Icon
snake=pygame.image.load('snake.jpg')
pygame.display.set_icon(snake)

# Variable for speed
x=17
    
# Play Surface
play_surface=pygame.display.set_mode((760,460))
pygame.display.set_caption('Snake Game!')

# Game Colors
red=pygame.Color(255,0,0)       #Game Over Message
green=pygame.Color(0,255,0)     #Snack
black=pygame.Color(0,0,0)       #Score
white=pygame.Color(255,255,255) #Background
brown=pygame.Color(165,42,42)   #Food
blue=pygame.Color(0,0,204)      #Background

# FPS Controller
fpsController=pygame.time.Clock()

#Important Variables
snakePos=[100,50]
snakeBody=[[100,50],[90,50],[80,50]]

foodPos=[random.randrange(1,72)*10,random.randrange(1,46)*10]
foodSpawn=True

direction = 'RIGHT'
changeto = direction

score=0

#Game Over function
def gameOver():
    pygame.mixer.music.stop()
    pygame.mixer.Sound.play(gameover_sound)
    myFont=pygame.font.SysFont('monospace',72)
    goSurface=myFont.render('Game Over!',True,red)
    goReact=goSurface.get_rect()
    goReact.midtop=(370,15)
    play_surface.blit(goSurface,goReact)
    showScore(0)
    pygame.display.flip()
    time.sleep(4)
    pygame.quit()    #pygame Exit
    sys.exit()       #System Exit
    
def showScore(choice=1):
    sFont=pygame.font.SysFont('monospace',30)
    sSurface=sFont.render('Score:'+str(score),True,black)
    sReact=sSurface.get_rect()
    if choice==1:
        sReact.midtop=(80,10)
    else:
        sReact.midtop=(360,100)
    play_surface.blit(sSurface,sReact)
    
    
# Main Logic
while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type==pygame.KEYDOWN:
            if(event.key==pygame.K_RIGHT or event.key==ord('d') or event.key==ord('D')):
                changeto='RIGHT'
            if(event.key==pygame.K_LEFT or event.key==ord('a') or event.key==ord('A')):
                changeto='LEFT'
            if(event.key==pygame.K_UP or event.key==ord('w') or event.key==ord('W')):
                changeto='UP'
            if(event.key==pygame.K_DOWN or event.key==ord('s') or event.key==ord('S')):
                changeto='DOWN'
            if(event.key==pygame.K_ESCAPE):
                pygame.event.post(pygame.event.Event(pygame.QUIT))
    # Direction Validation
    if changeto=='RIGHT' and not direction=='LEFT':
        direction='RIGHT'
    if changeto=='LEFT' and not direction=='RIGHT':
        direction='LEFT'
    if changeto=='UP' and not direction=='DOWN':
        direction='UP'
    if changeto=='DOWN' and not direction=='UP':
        direction='DOWN'
    
    # Update Snake Position
    if direction=='RIGHT':
        snakePos[0]+=10
    if direction=='LEFT':
        snakePos[0]-=10
    if direction=='UP':
        snakePos[1]-=10
    if direction=='DOWN':
        snakePos[1]+=10
                
    # Snack Body Mechanism
    snakeBody.insert(0,list(snakePos))
    if snakePos[0]==foodPos[0] and snakePos[1]==foodPos[1]:
        pygame.mixer.Sound.play(snakebit_sound)
        x+=1
        score+=1
        foodSpawn=False
    else:
        snakeBody.pop()
    # food Eating
    if foodSpawn == False:
        foodPos = [random.randrange(1,72)*10,random.randrange(1,46)*10]
    foodSpawn = True
   
    #Draw Snake
    play_surface.fill(green)
    for pos in snakeBody:
        pygame.draw.rect(play_surface,brown, pygame.Rect(pos[0],pos[1],10,10))
        
    # Draw Food
    pygame.draw.rect(play_surface,red, pygame.Rect(foodPos[0],foodPos[1],10,10))
    
    
    # Boundry
    if snakePos[0]>750 or snakePos[0]<0:
        pygame.mixer.music.stop()
        pygame.mixer.Sound.play(crash_sound)
        time.sleep(1)
        gameOver()
    if snakePos[1]>450 or snakePos[1]<0:
        pygame.mixer.music.stop()
        pygame.mixer.Sound.play(crash_sound)
        time.sleep(1)
        gameOver()
    
    # Hitting Itself
    for block in snakeBody[1:]:
        if snakePos[0]==block[0] and snakePos[1]==block[1]:
            pygame.mixer.music.stop()
            pygame.mixer.Sound.play(crash_sound)
            time.sleep(1)
            gameOver()
    
    
    showScore()
    pygame.display.flip()
    fpsController.tick(x)
        
    
                
                
                
                
                
                



