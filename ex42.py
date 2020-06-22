class Animal(object):
    pass

## Dog is-a Animal
class Dog(Animal):

    def __init__(self,name):
        ## ??
        self.name = name


## class Cat is-a Animal
class Cat(Animal):

    def __init__(self,name):
        ## class Cat has-a __init__ which has self and name paramenters
        self.name = name

    
## class Person is-a object
class Person(object):

    def __init__(self,name):
        ## class Person has-a __init__ which has self and name parameters
        self.name = name

        ## Person has-a pet of some kind
        self.pet = None


## class Employee is-a Person
class Employee(Person):

    def __init__(self,name,salary):
        ## class Employee has-a __init__ which has self,name and salary parameters
        super(Employee,self).__init__(name)
        ## Employee has-a salary
        self.salary = salary


## class Fish is-a object
class Fish(object):
    pass


## class Salmon is-a Fish
class Salmon(Fish):
    pass


## class Hilbot is-a Fish
class Halibut(Fish):
    pass


## rover is-a Dog
rover = Dog("Rover")


## satan is-a Cat
satan = Cat("Satan")

## mary is-a Person
mary = Person("Mary")

## mary has-a pet i.e satan
mary.pet = satan

## frank is-a Employee
frank = Employee("Frank",120000)

## frank has-a pet
frank.pet = rover

## flipper is-a Fish
flipper = Fish()

## crouse is-a Salmon
crouse = Salmon()

## harry is-a Halibut
harry = Halibut()


