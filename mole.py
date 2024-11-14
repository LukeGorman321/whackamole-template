import random
class Mole:
    x, y, xOffset, yOffset = 0,0,0,0
    bomb, naked = False, False
    time = 10.0
    def __init__(self, moles, bomb=False):
        self.new_position(moles)
        self.bomb = bomb
    def new_position(self, moles, tries = 0):
        self.x, self.y, self.xOffset, self.yOffset, self.time = random.randrange(0,20),random.randrange(0,16),random.randrange(-4,8),random.randrange(-4,8), random.uniform(8.0,12.0)
        if random.randrange(0,10) == 0:
            self.naked = True
        else:
            self.naked = False
        if tries < 100:
            for mole in moles:
                if ((mole.bomb and not self.bomb) or (self.bomb and not mole.bomb)) and self.x == mole.x and mole.y == self.y:
                    self.new_position(moles, tries + 1)
                    return
    def update_timer(self, screen, font,delta):
        self.time -= delta/1000
        if self.bomb:
            screen.blit(font.render(str(round(self.time)), False, "#ff0000"), 
            (self.x*32+7+self.xOffset + (0 if round(self.time) >= 10 else 6), self.y*32+10+self.yOffset))
        else:
            screen.blit(font.render(str(round(self.time,1)), False, "#903022"), 
            (self.x*32+20+self.xOffset if self.x < 19 else self.x*32-20+self.xOffset,
            self.y*32-3+self.yOffset if self.y > 0 else self.y*32 + 20 + self.yOffset))