class car:
    def __init__(self,brand,color,type):
        self.brand=brand
        self.color=color
        self.type=type
        print("Добавился машина:"+ self.brand, self.color,self.type)
        
car1=car("Tayoto","black","easy")