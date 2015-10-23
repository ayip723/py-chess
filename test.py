# def func1():
#     return "Arthur"
#
# print func1()


class C1(object):
    CONS = "ARTHUR"

    HORIZONTAL_DIRS = [
        [-1, 0],
        [0, -1],
        [0, 1],
        [1, 0]
    ]

    DIAGONAL_DIRS = [
        [-1, -1],
        [-1, 1],
        [1, -1],
        [1, 1]
    ]

    def horizontal_dirs():
        return HORIZONTAL_DIRS

    def diagonal_dirs():
        return DIAGONAL_DIRS

    def __init__(self):
        pass
    def f1(self):
        print "hello world!"
    def f2(self):
        self.f1()

c = C1()
c.f2()
c.CONS = "arthur"
print c.CONS

for x, y in [[1,2],[3,4]]:
    print x
    print y

for i in range(10):
    if i == 5: continue
    print i

print "-------------"

def square(a):
    return a ** 2

def add(a, b):
    return a + b
arr1 = [1, 2]
arr2 = [3, 4]
# print map(square, arr1)
print map(add, arr1, arr2)

print "--------------"

class C2(object):
    def __init__(self, arg1):
        print "Parent constructor"
        print arg1

    def m1(self):
        print "From parent"

class C3(C2):
    def __init__(self, arg1):
        super(C3, self).__init__(arg1)

    def m1(self):
        # super(C2, self).m1()
        super(C3, self).m1()
        # print super(C2).m1(self)
        print "From children"

c = C3("arg1")
c.m1()

print c

print "-------------"

class Car(object):
    condition = "new"
    def __init__(self, model, color, mpg):
        self.model = model
        self.color = color
        self.mpg   = mpg

    def display_car(self):
        return "This is a %s %s with %d MPG." % (self.color, self.model, self.mpg)

    def drive_car(self):
        self.condition = "used"

my_car = Car("DeLorean", "silver", 88)
print my_car.condition
print my_car.model
print my_car.color
print my_car.mpg

print my_car.display_car()

print my_car.condition
my_car.drive_car()
print my_car.condition
print Car.condition
Car.condition = "weird"
print Car.condition
my_car.attr1 = "attr1"
print my_car.attr1
