class Car:
    def __init__(self, speed: int = 0):
        self.speed = speed

    def accelerate(self, acceleration=1):
        self.speed += acceleration

    def brake(self, slowness=1):
        if self.speed > 0:
            self.speed -= slowness
        else:
            print('car stopped already!')

    def check_speedometer(self):
        return self.speed