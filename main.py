import pygame 
import time
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
        self.energy_ratio = self.maximum_energy / self.energy_bar_length
    
    def update(self):
        pass
    
    def get_time (self, amount):
        if self.current_energy > 0:
            self.current_energy -= amount
        if self.current_energy <= 0:
            self.current_energy = 0
    
    def get_sleep(self, amount):
        if self.current_energy < self.maximum_energy:
            self.current_energy += amount
        if self.current_energy >= self.maximum_energy:
            self.current_energy = self.maximum_energy

    
player = Player()

sleeping=False
#contributes to keeping the character from being too fast
vel = 2

            
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
            if event.key == pygame.K_SPACE and player.rect.colliderect(bed_rect):
                sleeping = True
                  
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
    if collide and keys[pygame.K_SPACE]:
            player.get_sleep(10)
            print("mimimimimi, i'm sleeping")
    
    #the screen
    pygame.draw.rect(window, (255, 0, 0), player.rect)
    
    pygame.display.flip()
    #contributes to keeping the character from being too fast
    clock.tick(60)
    
pygame.quit()
exit()  
            