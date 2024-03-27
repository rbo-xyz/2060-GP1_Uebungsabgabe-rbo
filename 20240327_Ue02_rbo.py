class Vector3:
    def __init__(self, x=0, y=0, z=0):
        self.x = x
        self.y = y
        self.z = z

    def __str__(self):
        return f"3D-Vektor = ({self.x}, {self.y}, {self.z})"

    def __add__(self, other):
        if type(other) == Vector3:
            return Vector3(self.x + other.x, self.y + other.y, self.z + other.z)
        elif type(other) == int or type(other) == float:
            return Vector3(self.x + other, self.y + other, self.z + other)

    def __sub__(self, other):
        if type(other) == Vector3:
            return Vector3(self.x - other.x, self.y - other.y, self.z - other.z)
        elif type(other) == int or type(other) == float:
            return Vector3(self.x - other, self.y - other, self.z - other)

    def __mul__(self, other):
        if type(other) == Vector3:
            return Vector3(self.x * other.x, self.y * other.y, self.z * other.z)
        elif type(other) == int or type(other) == float:
            return Vector3(self.x * other, self.y * other, self.z * other)
        else:
            return "Die Multiplikation kann mithilfe der eingebenen Datentypen nicht berechnet werden"

    def __rmul__(self, other):
        if type(other) == int or type(other) == float:
            return Vector3(self.x * other, self.y * other, self.z * other)
        else:
            return "Die Multiplikation kann mithilfe der eingebenen Datentypen nicht berechnet werden"

    def dot(self, other):
        if type(other) == Vector3:
            return self.x * other.x + self.y * other.y + self.z * other.z
        else:
            return "Das Skalarprodukt kann mithilfe der eingebenen Datentypen nicht berechnet werden"

    def cross(self, other):
        if type(other) == Vector3:
            return Vector3((self.y * other.z - self.z * other.y),
                           ((-1)*(self.x*other.z - self.z*other.x)),
                           (self.x * other.y - self.y * other.x))
        else:
            return "Das Kreuzproduktkann mithilfe der eingebenen Datentypen nicht berechnet werden"

    def normalize(self):
        lenV = (self.x**2 + self.y**2 + self.z**2)**0.5
        if lenV == 0:
            return "Der Vektor kann mit der Eingabe nicht normiert werden, da es sich um dem Nullvektor handelt"
        else:
            return Vector3(self.x/lenV, self.y/lenV, self.z/lenV)
        
    def lenVector3(self):
        return (self.x**2 + self.y**2 + self.z**2)**0.5

#Definiton der Testvektoren
a = Vector3(3, 4, 2)
b = Vector3(2, 1, 0)
c = Vector3(3, 5, 7)

print(type(a))
print(type(b))
print(type(c))

#Test addition, subtraktion, multiplikation (Skalar)
x1 = a + b 
print(x1)
x2 = b + 1
print(x2)

x3 = a - b 
print(x3)
x4 = b - 1
print(x4)

x5 = a * b 
print(x5)
x6 = 2 * b
print(x6)
x7 = b * 2
print(x7)

#Test des Skalarproduktes
print(a.dot(b))

#Test des Kreuzproduktes
print(a.cross(b))

#Test der Vektonormierung
x30 = a.normalize()
print(x30)
print(x30.lenVector3())