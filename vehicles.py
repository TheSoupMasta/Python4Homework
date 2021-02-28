class Vehicle:
    def __init__(self, top_speed):
        self.top_speed = top_speed
        self.speed = 0

    def accelerate(self, speed_change):
        self.speed += speed_change
        if self.speed > self.top_speed:
            self.speed = self.top_speed
            print("Going at max speed!")

    def brake(self, speed_change):
        self.speed -= speed_change
        if self.speed < 0:
            self.speed = 0
            print("We have come to a halt")

    def get_speed(self):
        return self.speed

class Car(Vehicle):
    def __init__(self, top_speed):
        super().__init__(top_speed)
        self.reversed = False

    def accelerate(self, speed_change):
        if self.reversed:
            if speed_change > 0:
                super(Car, self).accelerate(-speed_change)
            else:
                super(Car, self).accelerate(speed_change)
        else:
            if speed_change < 0:
                super(Car, self).accelerate(-speed_change)
            else:
                super(Car, self).accelerate(speed_change)

    def brake(self, speed_change):
        if self.reversed:
            if speed_change > 0:
                super(Car, self).brake(-speed_change)
            else:
                super(Car, self).brake(speed_change)
        else:
            if speed_change < 0:
                super(Car, self).brake(-speed_change)
            else:
                super(Car, self).brake(speed_change)

    def reverse(self):
        if self.get_speed() == 0:
            self.reversed = not self.reversed
        else:
            print("Can't reverse while moving!")



class Airplane(Vehicle):
    def __init__(self, top_speed):
        super().__init__(top_speed)
        self.is_flying = False

    def accelerate(self, speed_change):
        super().accelerate(speed_change)
        if not self.is_flying and self.get_speed() >= 250:
            self.is_flying = True
            print("Plane is taking off!")


    def brake(self, speed_change):
        super().brake(speed_change)
        if self.is_flying and self.get_speed() < 250:
            self.is_flying = False
            print("Plane has landed")


class Boat(Vehicle):
    def __init__(self, maxcapacity, top_speed):
        super(Boat, self).__init__(top_speed)
        self.maxcapacity = maxcapacity
        self.currentpassengers = 0

    def loadup(self, newpassengers):
        self.currentpassengers += newpassengers
        if self.currentpassengers >= self.maxcapacity:
            self.currentpassengers = self.maxcapacity
            print('Maximum safe occupancy reached.')

    def accelerate(self, speed_change):
        super().accelerate(speed_change)


    def brake(self):
        speed_change_slowing = self.currentpassengers
        super().brake(speed_change_slowing)
        if self.speed <= 0:
            self.speed = 0



# car = Car(250)
# print(car.get_speed())

# car.accelerate(15)
# car.brake(10)
# print(car.get_speed())
# car.accelerate(20)
# print(car.get_speed())
# car.brake(50)
# car.reverse()
# car.accelerate(50)
# print(car.get_speed())
#
#
# airplane = Airplane(600)
# airplane.accelerate(200)
# airplane.accelerate(250)
# print(airplane.get_speed())
# airplane.brake(300)


boat = Boat(100, 20)
boat.accelerate(5)
boat.loadup(75)
boat.brake()