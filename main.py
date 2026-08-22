import pygame 
print(pygame.version.ver)

pygame.init()
window = pygame.display.set_mode((300, 300))
clock = pygame.time.Clock()

rect = pygame.Rect(0, 0, 20, 20)
rect.center = window.get_rect().center
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
    keys = pygame.key.get_pressed()
    #user movement
    rect.x += (keys[pygame.K_RIGHT] - keys[pygame.K_LEFT]) * vel
    rect.y += (keys[pygame.K_DOWN] - keys[pygame.K_UP]) * vel
    #user starts at center
    rect.centerx = rect.centerx % window.get_width()
    rect.centery = rect.centery % window.get_height()
    
    window.fill(0)
    #this is the bed
    window.blit(bed, bed_rect)
    
    collide = pygame.Rect.colliderect(rect, bed_rect)
    if collide:
        print("hey, you've hit me!")
    
    #the screen
    pygame.draw.rect(window, (255, 0, 0), rect)
    
    pygame.display.flip()
    #contributes to keeping the character from being too fast
    clock.tick(60)
    
pygame.quit()
exit()  
            