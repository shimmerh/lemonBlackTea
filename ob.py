class Vector(object):
    
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        self.x += other.x
        self.y += other.y

        return self

    def __str__(self):
        return "({}, {})".format(self.x, self.y)



v1 = Vector(1,2)
v2 = Vector(2,3)

v3 = v1 + v2

print(v3)