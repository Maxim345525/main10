class profesional:
    Model = ''
    Company = ''
    def __init__(self):
        print("Create object Profesional")
        self.Model = 'Doctor'
        self.Company = 'Medilux'
    def ShowOn(self):
        print(self.Model)
        print(self.Company)
    def __del__(self):
        print("Delete object Profesional")
if __name__ == '__main__':
    profesional = profesional()
    profesional.ShowOn()
    del profesional