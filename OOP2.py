'''
class Remote:
    pass

class Player:
    def moveReverse(self):
        pass
    def moveForward(self):
        pass
    def moveRight(self):
        pass
    def moveLeft(self):
        pass

player1 = Player()
remote1 = Remote()

if(remote1.isLeftPressed()):
    player1.moveLeft()

'''
'''
# chatGPT: 

class Dog:
    def __init__(self, name):
        print(self.__getstate__())
        self.name = name
    def bark(self):
        print(f"{self.name} says woof!")

# my_dog = Dog("Buddy")
# my_dog.bark()  # Output: Buddy says woof!

class Labrador(Dog):
    print("whats in DOG",Dog)
    def bark(self):
        print(f"{self.name} says loud woof!")
        pass

my_labrador = Labrador("Max")
my_labrador.bark()  # Output: Max says loud woof!

'''

print('python'[1:5])