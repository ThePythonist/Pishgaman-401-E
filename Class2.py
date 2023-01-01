class A:
    def say_hello(self):
        print("Hello")


class B(A):
    def say_goodbye(self):
        print("Goodbye")


valed = A()
farzand = B()

farzand.say_goodbye()
farzand.say_hello()
