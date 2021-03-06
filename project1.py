import pygame as pg

class dog(pg.sprite.Sprite):

    def __init__(self):
        super(dog, self).__init__()

        self.images = []
        self.images.append(pg.image.load("dog/walk1.png"))
        self.images.append(pg.image.load("dog/walk2.png"))
        self.images.append(pg.image.load("dog/walk3.png"))
        self.images.append(pg.image.load("dog/walk4.png"))
        self.images.append(pg.image.load("dog/walk5.png"))
        self.images.append(pg.image.load("dog/walk6.png"))
        self.images.append(pg.image.load("dog/walk7.png"))
        self.images.append(pg.image.load("dog/walk8.png"))
        self.images.append(pg.image.load("dog/walk9.png"))
        self.images.append(pg.image.load("dog/walk10.png"))

        self.index = 0

        self.image = self.images[self.index]

        self.rect = pg.Rect(1, 1, 100, 150)
        self.image = pg.transform.scale(self.image, (120, 100))

    def update(self):
        key_states = pg.key.get_pressed()
        if key_states[pg.K_UP] or key_states[pg.K_DOWN] or key_states[pg.K_LEFT] or key_states[pg.K_RIGHT]:
            self.index += 1
            if self.index >= len(self.images):
                self.index = 0

            self.image = self.images[self.index]
            self.image = pg.transform.scale(self.image, (120, 100))

        if key_states[pg.K_UP] or key_states[pg.K_DOWN] or key_states[pg.K_LEFT] or key_states[pg.K_RIGHT]:
            pass

        else:
            self.image = self.images[1]
            self.image = pg.transform.scale(self.image, (120, 100))




pg.init()
screen = pg.display.set_mode((800, 800))
sprite = dog()
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
