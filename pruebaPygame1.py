import pygame

#default
SIZE = width , height = [640, 480]
SPEED_Chicken = [2,2]
SPEED_CristoRey = [1,1]
BLACK = 0,0,0

def adjust_CT(fps, SPEED):
    return [int(x * 60/fps) for x in SPEED]


def game(fps, chicken, cristo, screen):
    position_chicken = chicken.get_rect()
    position_cristo = cristo.get_rect()
    clock = pygame.time.Clock()
    while True:
        # check input
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                exit()
        # update game state
        position_chicken = position_chicken.move(adjust_CT(fps, SPEED_Chicken))
        if position_chicken.left < 0 or position_chicken.right > SIZE[0]:
            SPEED_Chicken[0] = -SPEED_Chicken[0]
        if position_chicken.top < 0 or position_chicken.bottom > SIZE[1]:
            SPEED_Chicken[1] = -SPEED_Chicken[1]

        position_cristo = position_cristo.move(adjust_CT(fps, SPEED_CristoRey))
        if position_cristo.left < 0 or position_cristo.right > SIZE[0]:
            SPEED_CristoRey[0] = -SPEED_CristoRey[0]
        if position_cristo.top < 0 or position_cristo.bottom > SIZE[1]:
            SPEED_CristoRey[1] = -SPEED_CristoRey[1]

        # draw game objects
        screen.fill(BLACK)
        screen.blit(chicken, position_chicken)
        screen.blit(cristo, position_cristo)
        pygame.display.flip()
        # wait for fps
        clock.tick(fps)


if __name__ == "__main__":
    pygame.init()
    screen = pygame.display.set_mode(SIZE)
    chicken = pygame.image.load("chicken.png")
    cristo = pygame.image.load("cristo_rey.png")
    game(60, chicken, cristo, screen)

