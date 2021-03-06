import pygame as pg

class Walkingpumpkinguy(pg.sprite.Sprite):

    def __init__(self):
        super(Walkingpumpkinguy, self).__init__()

        self.images = []
        self.images.append(pg.image.load("images/walk1.png"))
        self.images.append(pg.image.load("images/walk2.png"))
        self.images.append(pg.image.load("images/walk3.png"))
        self.images.append(pg.image.load("images/walk4.png"))
        self.images.append(pg.image.load("images/walk5.png"))
        self.images.append(pg.image.load("images/walk6.png"))
        self.images.append(pg.image.load("images/walk7.png"))
        self.images.append(pg.image.load("images/walk8.png"))
        self.images.append(pg.image.load("images/walk9.png"))
        self.images.append(pg.image.load("images/walk10.png"))

        self.index = 0

        self.image = self.images[self.index]

        self.rect = pg.Rect(5, 5, 150, 198)

    def update(self):
        self.index += 1
        if self.index >= len(self.images):
            self.index = 0

        self.image = self.images[self.index]

pg.init()
screen = pg.display.set_mode((400, 400))
sprite = Walkingpumpkinguy()
group = pg.sprite.Group(sprite)

clock = pg.time.Clock()

running = True

while running:

    screen.fill((10, 255, 10))
    group.update()
    group.draw(screen)
    pg.display.update()
    clock.tick(10)

    events = pg.event.get()
    for event in events:
        if event.type == pg.QUIT:
            pg.quit()
            running = False
