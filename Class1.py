class Car:
    def __init__(self, m, hp, c):
        self.model = m
        self.hp = hp
        self.color = c

    def horn(self):
        print("Booooogh")

    def brreak(self):
        print("Eeeeh")


dena = Car("1401", 130, "Black")
samand = Car("1399", 120, "White")

# dena.horn()
# samand.horn()
# dena.brreak()
# samand.brreak()

print(dena.model)
print(samand.hp)
