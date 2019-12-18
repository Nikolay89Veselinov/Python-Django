class Human:
    def say_hello(self):
        print("Hello! I am a human!")

class Niki(Human):
    def say_hello(self):
        super().say_hello()
        print("Hello! I am Niki")


niki_obj = Niki()
niki_obj.say_hello()
