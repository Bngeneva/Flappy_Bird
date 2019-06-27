import random, pygame, sys
from pygame.locals import *
from Dragon_Class import Dragon
from Rock_Class import Rock

pygame.init()
screen_info = pygame.display.Info()

size = (width, height) = (int(screen_info.current_w), int(screen_info.current_h))
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()


background = pygame.image.load('Flappy_Bird_Landscape.png')
background = pygame.transform.scale(background, (width, height))

color = (0, 0, 0)

startPos = (width / 8, height / 2)
rocks = pygame.sprite.Group()
player = Dragon(startPos)
gapSize = 200
loopCount = 0

def lose():
    font = pygame.font.SysFont(Pacifico, 70)
    text = font.render("Your Dragon has been knocked out!", True, (255, 255, 255))
    text_rect = text.get_rect()
    text_rect.center = (width/2, height/2)
    while True:
        screen.fill(color)
        screen.blit(text, text_rect)
        pygame.display.flip()
        for event in pygame.event.get():
            if event.key == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    rocks.empty()
                    player.reset(startPos)
                    return

def main():
    global loopCount
    while True:
        if loopCount % 90 == 0:
            topPos = random.randint(0, height/2) - 400
            rocks.add(Rock((width + 100, topPos + gapSize + 800)))
            rocks.add(Rock((width + 100, topPos), True))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.type == pygame.K_SPACE:
                    player.speed[1] = -10
        player.update()
        rocks.update()
        collision = pygame.sprite.spritecollide(player, rocks, False) or player.rect.center[1] > height
        screen.blit(background, [0, 0])
        rocks.draw(screen)
        screen.blit(player.image, player.rect)
        pygame.display.flip()
        loopCount += 1

        if collision:
            lose()

if __name__ == '__main__':
    main()


