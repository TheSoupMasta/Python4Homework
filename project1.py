import pygame as pg

class dog(pg.sprite.Sprite):

    def __init__(self):
        super(dog, self).__init__()
        #defining images sets
        self.images = []
        self.runimages = []

        #defining the images within the sets
        for i in range(1, 11):
            self.images.append(pg.image.load("dog/" + "walk" + str(i) + ".png"))

        for i in range(1, 9):
            self.runimages.append(pg.image.load("dog/run" + " (" + str(i) + ")" + ".png"))


        #defining the different animations
        self.animations = {
            "running" : self.runimages,
            "walking" : self.images
        }


        #defining variables
        self.current_animation = self.images
        self.frame_index = 0
        self.image = self.images[self.frame_index]
        self.animationset = "walking"

        self.rect = pg.Rect(10, 10, 120, 100)
        self.image = pg.transform.scale(self.image, (120, 100))
        self.facingright = False


    def update(self):
        #starting animations when key is pressed
        key_states = pg.key.get_pressed()
        if key_states[pg.K_w] or key_states[pg.K_s] or key_states[pg.K_a] or key_states[pg.K_d]:
            self.frame_index += 1
            if self.frame_index >= len(self.current_animation):
                self.frame_index = 0

            #changes speed for walking
            if self.animationset == "walking":
                if key_states[pg.K_w]:
                    self.rect = self.rect.move(0, -10)
                if key_states[pg.K_s]:
                    self.rect = self.rect.move(0, 10)
                if key_states[pg.K_a]:
                    self.rect = self.rect.move(-10, 0)
                if key_states[pg.K_d]:
                    self.rect = self.rect.move(10, 0)
            #changes speed for running
            if self.animationset == "running":
                if key_states[pg.K_w]:
                    self.rect = self.rect.move(0, -20)
                if key_states[pg.K_s]:
                    self.rect = self.rect.move(0, 20)
                if key_states[pg.K_a]:
                    self.rect = self.rect.move(-20, 0)
                if key_states[pg.K_d]:
                    self.rect = self.rect.move(20, 0)

            self.image = self.current_animation[self.frame_index]
            self.image = pg.transform.scale(self.image, (120, 100))
            if self.facingright == False:
                self.image = pg.transform.flip(self.image, True, False)

        #resetting images to the first frame of animation when stopped pressing
        else:
            self.image = self.current_animation[1]
            self.image = pg.transform.scale(self.image, (120, 100))
            if self.facingright == False:
                self.image = pg.transform.flip(self.image, True, False)

        #Flipping images when walking diagnally or normally
        if key_states[pg.K_w] and key_states[pg.K_d]:
            self.facingright = True
        elif key_states[pg.K_s] and key_states[pg.K_d]:
            self.facingright = True

        elif key_states[pg.K_w] and key_states[pg.K_a]:
            self.facingright = False
        elif key_states[pg.K_s] and key_states[pg.K_a]:
            self.facingright = False

        elif key_states[pg.K_a]:
            self.facingright = False

        elif key_states[pg.K_d]:
            self.facingright = True



    #setting new animation when shift key is pressed or not pressed
    def set_animation(self, key, animset):
        #setting animations to the correct sets
        self.current_animation = self.animations[key]
        self.animationset = animset


#Initalizing some stuff, don't mind this
pg.init()
screen = pg.display.set_mode((600, 600), pg.RESIZABLE)
sprite = dog()
group = pg.sprite.Group(sprite)

clock = pg.time.Clock()

running = True

#detects events and sets up some important variables when launched
while running:

    screen.fill((10, 255, 10))
    group.update()
    group.draw(screen)
    pg.display.update()
    clock.tick(20)

    events = pg.event.get()
    for event in events:
        if event.type == pg.QUIT:
            pg.quit()
            running = False
        #checks if shift key is pressed or not pressed to change the image sets (see rest of code in def set_animation)
        if event.type == pg.KEYDOWN and (event.key == pg.K_LSHIFT or event.key == pg.K_RSHIFT):
            sprite.set_animation("running", "running")
        if event.type == pg.KEYUP and (event.key == pg.K_LSHIFT or event.key == pg.K_RSHIFT):
            sprite.set_animation("walking", "walking")

