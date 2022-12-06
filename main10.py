class Guitar:
    Model = ''
    Company = ''
    w = 0
    h = 0
    d = 0
    def __init__(self):
        print("Create object Guitar")
        self.Model = 'Ukulele'
        self.Company = 'Guitar'
        self.d = 10.3
        self.h = 7.5
        self.w = 70
    def ShowOn(self):
        print(self.Model)
        print(self.Company)
        print(self.d)
        print(self.h)
        print(self.w)
    def __del__(self):
        print("Delete object Guitar")
if __name__ == '__main__':
    guitar = Guitar()
    guitar.ShowOn()