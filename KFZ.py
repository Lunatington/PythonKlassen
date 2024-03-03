class KFZ:
    def __init__(self, tires, fuel, hp):
        self.tires = tires
        self.fuel = fuel
        self.hp = hp
    
    def information(self):
        print(f"tires = {self.tires}")
        print(f"fuel = {self.fuel}")
        print(f"horsepower = {self.hp}")
        
