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
