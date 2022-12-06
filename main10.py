class Car:
    Model = ''
    Company = ''
    w = 0
    h = 0
    d = 0
    def __init__(self):
        print("Create object Car")
        self.Model = 'Model X'
        self.Company = 'Tesla'
        self.d = 150
        self.h = 345
        self.w = 564
    def ShowOn(self):
        print(self.Model)
    def ShowOn(self):
        print(self.Company)
    def ShowOn(self):
        print(self.d)
    def ShowOn(self):
        print(self.h)
    def ShowOn(self):
        print(self.w)
    def __del__(self):
        print("Delete object Car")
if __name__ == '__main__':
    car = Car()
    car.ShowOn()
    del car