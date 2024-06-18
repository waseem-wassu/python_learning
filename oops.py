#    Object oriented programming

'''
Solving a problem by creating objects is one of thempst popular approaches in programming. Thi is called oop

This concept focuses on using reusable code -> Implements DRY(Dono
t repeat yourself) principle
'''


#Class : A class is a blueprint for creating objects
'''
syntax 

class employee:
    # Methods and variables
'''

class Student:
    def myFunc(self):
        print(self.name,self.__getattribute__('age'))
        print("To get what is there inside the object",self.__getstate__())

user1 = Student()
user1.name = "waseem"
user1.age = 25
user1.myFunc()

    

