class Vector:
    def __init__(self, x=0, y=0):
        self._x = x
        self._y = y

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, value):
        self._x = value

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, value):
        self._y = value

    def __add__(self, other):
        if isinstance(other, Vector):
            return Vector(self.x + other.x, self.y + other.y)
        raise TypeError("Operands must be of type Vector")

    def __sub__(self, other):
        if isinstance(other, Vector):
            return Vector(self.x - other.x, self.y - other.y)
        raise TypeError("Operands must be of type Vector")

    def __str__(self):
        return f"Vector({self.x}, {self.y})"

    def __repr__(self):
        return f"Vector({self.x}, {self.y})"

    def __eq__(self, other):
        if isinstance(other, Vector):
            return self.x == other.x and self.y == other.y
        return False

    def __mul__(self, scalar):
        if isinstance(scalar, (int, float)):
            return Vector(self.x * scalar, self.y * scalar)
        raise TypeError("Operand must be a number")

    def __rmul__(self, scalar):
        return self.__mul__(scalar)


v1 = Vector(2, 3)
v2 = Vector(1, 1)

print("v1:", v1)  
print("v2:", v2)  

v3 = v1 + v2
print("v1 + v2:", v3)  

v4 = v1 - v2
print("v1 - v2:", v4)  

v5 = v1 * 3
print("v1 * 3:", v5)  

v6 = 2 * v2
print("2 * v2:", v6)  

print("v1 == v2:", v1 == v2)  
print("v1 == Vector(2, 3):", v1 == Vector(2, 3)) 

v1.x = 5
v1.y = 6
print("Updated v1:", v1)  
