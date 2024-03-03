class KFZ:
    def __init__(self, tires, fuel, hp):
        self.tires = tires
        self.fuel = fuel
        self.hp = hp
    
    def information(self):
        print(f"tires = {self.tires}")
        print(f"fuel = {self.fuel}")
        print(f"horsepower = {self.hp}")
        
class PKW(KFZ):
    def __init__(self, tires, fuel, hp):
        super().__init__(tires, fuel, hp)
        
    def illegalestuning(self, number):
        self.hp += number
        
class LKW(KFZ):
    def __init__(self, tires, fuel, hp):
        super().__init__(tires, fuel, hp)
        
dreierbmw = KFZ(4,'Super', 99)
dreierbmw.information()