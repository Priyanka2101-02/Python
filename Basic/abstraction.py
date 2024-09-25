class Car:
    def __init__(self):
        self.acc = False
        self.brk = False
        self.gear = False
    def start(self):
        self.acc = True
        self.brk = True
        print("car Started!")

c1 = Car()
c1.start()
