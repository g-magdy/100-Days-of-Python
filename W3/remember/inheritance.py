class Animal:
    def __init__(self) -> None:
        self.weight = 20
        self.sound = ""
        self.num_eyes = 2
        
    def breathe(self):
        print("Ohhhhhmmmmm")
        
class Fish(Animal):
    def __init__(self) -> None:
        super().__init__()
        
    def breathe(self):
        super().breathe()
        
    def swim(self):
        print("water")
        
nemo = Fish()
nemo.breathe()
