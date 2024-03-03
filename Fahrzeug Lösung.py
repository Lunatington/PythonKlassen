from abc import ABC, abstractmethod

class Fahrzeug(ABC):
    def __init__(self):
        super().__init__()
        
    @abstractmethod
    def starten(self):
        pass
    
class Auto(Fahrzeug):
    def __init__(self):
        super().__init__()
        
    def starten(self):
        print("Auto wurde gestartet")