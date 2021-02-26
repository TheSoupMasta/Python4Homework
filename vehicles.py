class Vehicle:
    #defining __init__ function
    def __init__(self, speed, maxSpeed, color):
        self.speed = speed
        self.maxSpeed = maxSpeed
        self.color = color
        self.speed = 0

    #defining accelerate function
    def accelerate(self):
        self.speed += 100
        if self.speed >= self.maxSpeed:
            self.speed = self.maxSpeed
            print("The maximum speed of this vehicle has been achieved.")
        print("speed is: ", self.speed)

    #defining braking function
    def brake(self):
        self.speed -= 50
        if self.speed <= 0:
            self.speed = 0
            print("The slowest speed of this vehicle has been achieved.")
        print("speed is: ", self.speed)

    #defining upsize function
    def upsize(self):
        self.size = self.size + 10
        print("size is: ", self.size)


class Car(Vehicle):
    #defining __init__ function
    def __init__(self, speed, maxSpeed, color, isreversed):
        #using super call to inherit from other class and changed the max speed to 120
        super(Car, self).__init__(speed, maxSpeed, color)
        self.maxSpeed = 120
        self.isreversed = isreversed

    #defining accelerate function to override
    def accelerate(self):
        if self.isreversed == True:
            self.speed += 20
            if self.speed >= self.maxSpeed:
                self.speed = self.maxSpeed
                print("The maximum speed of this vehicle has been achieved.")
            print("speed is: ", self.speed)

        if self.isreversed == True and self.speed > 0:
            self.isreversed = False
            print("Reverse has deactivated")
        elif self.isreversed == False:
            self.speed -= 20


    #defining braking function to override
    def brake(self):
        self.speed -= 5
        if self.speed <= 0:
            self.isreversed = True
            self.speed = self.speed
            print("Reverse has activated")
        print("speed is: ", self.speed)


    #defining a reversing command
    def reverse(self):
        if self.isreversed == False:
            self.isreversed = True


    #gets current speed
    def getcurrentspeed(self):
        print("speed is: ", self.speed)


class Airplane(Vehicle):
    #defining the __init__ function
    def __init__(self, speed, maxSpeed, color, isflying):
        #using super call to inherit from other class and changed the max speed to 120
        super(Airplane, self).__init__(speed, maxSpeed, color)
        self.maxSpeed = 1000
        self.isflying = isflying

    #defining the acceleration function
    def accelerate(self):
        self.speed += 100
        if self.speed >= self.maxSpeed:
            self.speed = self.maxSpeed
            print("The maximum speed of this vehicle has been achieved.")
        print("speed is: ", self.speed)
        if self.speed >= 250:
            self.isflying = True
            print("The plane is in the sky")

        elif self.speed < 250:
            self.isflying = False
            print('The plane is landed')

    #defining braking function to override
    def brake(self):
        self.speed -= 50
        if self.speed <= 0:
            self.speed = 0
            print("The slowest speed of this vehicle has been achieved.")
        print("speed is: ", self.speed)

        if self.speed >= 250:
            self.isflying = True
            print("The plane is in the sky")

        elif self.speed < 250:
            self.isflying = False
            print('The plane is landed')
    #defining getting speed
    def getcurrentspeed(self):
        print("speed is: ", self.speed)

Car1 = Car(0, 120, "white", False)
Car1.getcurrentspeed()
Car1.brake()
Car1.brake()
Car1.brake()
Car1.brake()
Car1.brake()
Car1.accelerate()
Car1.accelerate()


Plane1 = Airplane(0, 1000, "red", False)


