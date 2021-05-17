class Dog:
    type="Mammals"
    def __init__(self,name,barksound):
     self.name=name
     self.barksound=barksound

    def puppy(self):
        return f"My pet is known as {self.barksound}"

    def play(self):
        return f"Puppy fetch {self.barksound}"

