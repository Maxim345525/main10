class Phone:
    Model = ''
    Company = ''
    w = 0
    h = 0
    d = 0
    def __init__(self):
        print("Create object Phone")
        self.Model = 'XS Max'
        self.Company = 'iPhone'
        self.d = 6.5
        self.h = 1.3
        self.w = 3
    def ShowOn(self):
        print(self.Model)
        print(self.Company)
        print(self.d)
        print(self.h)
        print(self.w)
    def __del__(self):
        print("Delete object Phone")
if __name__ == '__main__':
    phone = Phone()
    phone.ShowOn()
    del phone