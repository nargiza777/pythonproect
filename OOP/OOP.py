class Car:
    def __init__(self,color,style,max_speed):
        self.color = color
        self.style = style
        self.max_speed = max_speed
        self.speed = 0
    def start(self):
        print("{} car is starting".format(self.color))
        print("Broom broom")
    def stop(self):
        print("IIIIIHHHHH")
    def accel(self):
        print("HHHHHHHHhhhhhhh")
        print("maximum speed is {}".format(self.max_speed))
        self.speed+=10
    def status(self):
        print("The current speed of the {} car is {} mph".format(self.color,self.speed))

blue_car = Car("blue","Wagon","150")
ugly_car = Car("Mustard","SUV","180")

blue_car.start()
blue_car.accel()
blue_car.status()
blue_car.accel()