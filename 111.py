class Person:
    def __init__(self, fn, ln, a):
        self.firstname = fn
        self.lastname = ln
        self.age = a

    def talk(self):
        print(f"Salam man {self.firstname} hastam va {self.age} sal daram")


arshia = Person("Arshia", "Vaziri", 21)
arshia.talk()
