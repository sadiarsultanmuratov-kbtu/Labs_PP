class car:
    def __init__(self,brand,color,year):
        self.brand=brand
        self.color=color
        self.year=year
    def __str__(self):
        return f"Это О машине: {self.brand}, {self.color},{self.year}"

car1=car("Tayoto","red",2)
car2=car("BMW","white",4)
print(car1)
print(car2)