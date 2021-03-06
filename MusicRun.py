# Import a library of functions called 'pygame'
import pygame
import random
from Draw import *

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
DARK_GREEN = (0, 60, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
PURPLE = (200, 0, 255)
YELLOW = (255, 255, 0)

SCREEN_WIDTH = 700
SCREEN_HEIGHT = 500
GROUND = 250 #pixel ground level

mod = 0
        
def main():
    
    pygame.init()# Initialize the game engine

    size = (700, 500)   #Window Size
    screen = pygame.display.set_mode(size)  #Window Creation
    pygame.display.set_caption("MusicRun")  #Displays Window Title

    
    done = False # Loop until the user clicks the close button.

    clock = pygame.time.Clock() # Used to manage how fast the screen updates
    
    velocity = 4 #speed of character

    cloudX, cloudY = SCREEN_WIDTH, random.randrange(10, 100) #Starting pos of clouds
    floorX_1, floorX_2 = 0, 700 #Placement of grass running surface
    player = Player()   #Creation of player object
    mod = [0] #determines how fast scenery moves

    pygame.mixer.music.load('A Wish.ogg')   #Loads song into pygame
    pygame.mixer.music.set_endevent(pygame.constants.USEREVENT)     #A trigger event for when song ends
    pygame.mixer.music.play(50) #!?!?Not a permenent solution for infinite loop!?!?    

    jump_sound = pygame.mixer.Sound("spin_jump.wav") #Jump Sound

    floor_1 = pygame.image.load("Grass.png").convert()  #loads Grass Platform
    floor_2 = pygame.image.load("Grass.png").convert()  #loads Grass Platform


    #---Main Program Loop-------------------------------

    while not done:
        
        # --- Main event loop---------------------------

        for event in pygame.event.get(): # User did something
            if event.type == pygame.QUIT: # If user clicked close
                done = True # Flag that we are done so we exit this loop

        #---Updates Screen with new drawings------------
                
        screen.fill(WHITE) #Clears screen to white

        pygame.draw.rect(screen, (100,100,200), [0, 0, SCREEN_WIDTH, SCREEN_HEIGHT - 150]) #Sky Backdrop
        
        #pygame.draw.rect(screen, GREEN, [0, 350, 700, 200]) #Floor drawn
        
        screen.blit(floor_1,(floorX_1, 350))    #Draws Grass to screen
        screen.blit(floor_2,(floorX_2, 350))    #Draws Grass to screen
        
        player.draw(screen) #Draws player to screen
        
        pygame.draw.rect(screen, WHITE, [cloudX, cloudY, 50, 30]) #Cloud Drawn

        #---Player's Behavior----------------------------

        player.update(mod)
        
        #---Ground Behavior------------------------------

        floorX_1 -= 1 + mod[0]
        floorX_2 -= 1 + mod[0]

        if(floorX_1 <= -700):
            floorX_1 = 700
        if(floorX_2 <= -700):
            floorX_2 = 700
    
        #---Cloud Behavior------------------------------
    
        cloudX -= .5 + mod[0] #Moves Cloud to the left plus how fast the character is going

        if (cloudX < -50):  #When Cloud moves off left screen, respawn on right side
            cloudX = SCREEN_WIDTH
            cloudY = random.randrange(10, 100)

        #---Handles all key down events-----------------

        player.handle_keys(mod)
    
        #---Updates the screen with what we've drawn----

        pygame.display.flip()
        
        #---Limit to 60 frames per second---------------

        clock.tick(60)

    pygame.quit()
    
main()
