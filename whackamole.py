import pygame
import random
from mole import Mole

def main():
    try:
        pygame.init()
        pygame.font.init()
        font = pygame.font.SysFont("Times New Roman", 15)
        gameOverFont = pygame.font.SysFont("Times New Roman", 70)
        scoreFont = pygame.font.SysFont("Times New Roman", 30)

        mole_image = pygame.image.load("mole.png")
        bomb_image = pygame.image.load("bomb.png")
        naked_mole_rat_image = pygame.image.load("nakedmole.png")

        screen = pygame.display.set_mode((640, 512))
        clock = pygame.time.Clock()
        running = True
        moles = [Mole([])]
        prevTicks = pygame.time.get_ticks()
        score = 0
        molesClicked = 0
        maxScore = 0
        exit = False
        while running:
            ticks = pygame.time.get_ticks()
            delta = ticks - prevTicks
            prevTicks = ticks
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    exit = True
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouseX, mouseY = event.pos
                    clickedX, clickedY = mouseX//32, mouseY//32
                    for mole in moles:
                        if mole.x == clickedX and mole.y == clickedY:
                            mole.new_position(moles)
                            if not mole.bomb:
                                score += 1
                                molesClicked += 1
                                if maxScore < score:
                                    maxScore = score
                                if molesClicked == len(moles) * 10:
                                    moles.append(Mole(moles))
                                    if random.randrange(0,5) == 0:
                                        moles.append(Mole(moles,True))
                            else:
                                score -= 15
                                if score < 0:
                                    running = False
            screen.fill("light green")
            for i in range(1,20):
                pygame.draw.line(screen, "#000000", (32*i,0), (32*i,512))
            for i in range(1,16):
                pygame.draw.line(screen, "#000000", (0,32*i), (640,32*i))
            for mole in moles:
                screen.blit((mole_image if not mole.naked else naked_mole_rat_image )if not mole.bomb else bomb_image, mole_image.get_rect(topleft=(mole.x*32+mole.xOffset,mole.y*32+mole.yOffset)))
                mole.update_timer(screen,font,delta)
                if mole.time <= 0:
                    mole.new_position(moles)
                    if not mole.bomb:
                        score -= 8 if not mole.naked else 20
                        if score < 0:
                            running = False 
            pygame.display.flip()
            clock.tick(60)
        while not exit:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit = True
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouseX, mouseY = event.pos
                    if mouseY > 400 and mouseY < 430 and mouseX > 200 and mouseX < 260:
                        exit = True
            screen.fill("light green")
            screen.blit(gameOverFont.render("Game Over!", False, "#cc0000"), (150,160))
            screen.blit(scoreFont.render("You have been overrun by moles!", False, "#000000"), (130,280))
            screen.blit(scoreFont.render("Your highest score was: " + str(maxScore), False, "#000000"), (170,320))
            screen.blit(scoreFont.render("You whacked " + str(molesClicked) + " moles!", False, "#000000"), (180,360))
            screen.blit(scoreFont.render("Click here to exit the game", False, "#000000"), (150,400))
            pygame.display.flip()
            clock.tick(10)
    finally:
        pygame.quit()


if __name__ == "__main__":
    main()

# How to play: (pause to read)
# Click on moles to whack them.
# You get a point each time you whack a mole.

# Each mole has a timer attached to it that lasts 8-12 seconds.
# If you don't whack the mole before its timer runs out, you lose 8 points.
# If you have less than zero points, you lose.

# Every 10 moles you whack an additional mole will spawn.
# Each time this happens, there is a 20% chance of a bomb spawning.
# If you click a bomb, you lose 15 points.

# Every mole has a 10% chance of spawning as a naked mole rat.
# The naked mole rats are especially devious rats.
# If you don't click them before their timer runs out, you lose 20 points.