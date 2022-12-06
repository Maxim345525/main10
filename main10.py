class Poshta:
    Model = ''
    Company = ''
    w = 0
    h = 0
    d = 0
    def __init__(self):
        print("Create object Poshta")
        self.Model = '#3'
        self.Company = 'Poshta'
        self.d = 15
        self.h = 56
        self.w = 32
    def ShowOn(self):
        print(self.Model)
        print(self.Company)
        print(self.d)
        print(self.h)
        print(self.w)
    def __del__(self):
        print("Delete object Poshta")
if __name__ == '__main__':
    poshta = Poshta()
    poshta.ShowOn()
    del poshta