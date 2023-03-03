import pygame

pygame.init()
#Set game constants
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 600
ROUND_TIME = 25

BLACK = (0,0,0)
WHITE = (255,255,255)
PLAYER_COLOR = (125, 55, 200)

FPS = 30
clock = pygame.time.Clock()
font = pygame.font.SysFont('gabriola', 28)

display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("~~Pygame Tutorial~~")


class Player():
    def __init__(self,x,y,size,color):
        self.x = x
        self.y = y
        self.size = size
        self.color = color

        self.dx = 0
        self.dy = 0
        self.coord = (self.x,self.y,self.size,self.size)

    def update(self):
        keys = pygame.key.get_pressed()
        player_rect = pygame.draw.rect(display_surface, self.color, self.coord)
        # Move the player
        if keys[pygame.K_UP] and player_rect.top > 0:
            self.dx = 0
            self.dy = -1 * self.size
        elif keys[pygame.K_DOWN] and player_rect.bottom < WINDOW_HEIGHT:
            self.dx = 0
            self.dy = 1 * self.size
        elif keys[pygame.K_LEFT] and player_rect.left > 0:
            self.dx = -1 * self.size
            self.dy = 0
        elif keys[pygame.K_RIGHT] and player_rect.right < WINDOW_WIDTH:
            self.dx = 1 * self.size
            self.dy = 0
        else:
            self.dx = 0
            self.dy = 0

        self.x += self.dx
        self.y += self.dy
        self.coord = (self.x, self.y, self.size, self.size)


class Game:
    def __init__(self,player):
        self.player = player
        self.frame_count = 0
        self.round_time = ROUND_TIME

    def update(self):
        self.frame_count += 1
        if self.frame_count % FPS  == 0:
            self.round_time -= 1
            self.frame_count = 0

        self.player.update()


    def draw(self):
        '''Draw the game and game assets to the game window'''
        #Draw the player
        pygame.draw.rect(display_surface, self.player.color, self.player.coord)

        #Create the round time text and draw
        time_text = font.render(f"Time: {self.round_time}", True, WHITE)
        time_rect = time_text.get_rect()
        time_rect.center = (WINDOW_WIDTH//2, 15)
        display_surface.blit(time_text, time_rect)

#Create a Player and Game class
my_player = Player(0,0,25,PLAYER_COLOR)
my_game = Game(my_player)

#The main game loop
running = True
while running:
    #Check to see if the user wants to quit
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #Fill the surface
    display_surface.fill(BLACK)

    #Update and draw classes
    my_game.update()
    my_game.draw()

    #Update the display and tick the clock
    pygame.display.update()
    clock.tick(FPS)




