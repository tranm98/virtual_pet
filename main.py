import pygame 
print(pygame.version.ver)

pygame.init()
window = pygame.display.set_mode((300, 300))
clock = pygame.time.Clock()

class Player():
    def __init__(self):
        self.rect = pygame.Rect(0, 0, 20, 20)
        self.rect.center = window.get_rect().center
        self.current_energy = 75
        self.maximum_energy = 100
        self.energy_bar_length = 100
        self.energy_ratio = self.maximum / self.energy_bar_length
    
    def update(self):
        pass
    
player = Player()
#contributes to keeping the character from being too fast
vel = 2

def get_energy(self, amount):
    if self.

time = pygame.time.get_ticks()
print(time)


bed = pygame.image.load("bed.png")
bed = pygame.transform.scale(bed,(80,50))

bed_rect = bed.get_rect()
bed_rect.topleft = (50,50)


run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            print(pygame.key.name(event.key))
    keys = pygame.key.get_pressed()
    #user movement
    player.rect.x += (keys[pygame.K_RIGHT] - keys[pygame.K_LEFT]) * vel
    player.rect.y += (keys[pygame.K_DOWN] - keys[pygame.K_UP]) * vel
    #user starts at center
    player.rect.centerx = player.rect.centerx % window.get_width()
    player.rect.centery = player.rect.centery % window.get_height()
    
    window.fill(0)
    #this is the bed
    window.blit(bed, bed_rect)
    
    collide = player.rect.colliderect(bed_rect)
    if collide:
        print("hey, you've hit me!")
    
    #the screen
    pygame.draw.rect(window, (255, 0, 0), player)
    
    pygame.display.flip()
    #contributes to keeping the character from being too fast
    clock.tick(60)
    
pygame.quit()
exit()  
            