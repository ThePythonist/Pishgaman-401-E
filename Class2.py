# class A:
#     def say_hello(self):
#         print("Hello")
#
#
# class B(A):
#     def say_goodbye(self):
#         print("Goodbye")
#
#
# valed = A()
# farzand = B()
#
# farzand.say_goodbye()
# farzand.say_hello()


class Father():
    def __init__(self, address, eyecolor, fname):
        self.familyname = fname
        self.address = address
        self.eyecolor = eyecolor

    def say_hello(self):
        print("Hello")


class Child(Father):
    def __init__(self, address, eyecolor, fname, age):
        super().__init__(fname, address, eyecolor)
        self.age = age

    def say_goodbye(self):
        print("Goodbye")


pedar = Father("Ahmadi", "Jomhori St", "Green")
pesar = Child("Ahmadi", "Jomhori St", "Green", 16)
print(pesar.eyecolor)
print(pesar.age)
