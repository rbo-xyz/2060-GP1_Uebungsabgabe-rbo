import math

class Figur: 
   def __init__(self, name): 
      self.name = name 
 
   def Umfang(self): 
        return 0 
 
   def __str__(self): 
      return self.name

class Punkt:
    def __init__ (self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"Punkt ({self.x}, {self.y})"

#---------------------------------------------

class Dreieck(Figur):
    def __init__ (self, pkt1, pkt2, pkt3):
        super().__init__("Dreieck")
        self.p1 = pkt1
        self.p2 = pkt2
        self.p3 = pkt3

    def Umfang(self):
        self.sd1 = ((self.p2.y - self.p1.y)**2 + (self.p2.x - self.p1.x)**2)**0.5
        self.sd2 = ((self.p3.y - self.p2.y)**2 + (self.p3.x - self.p2.x)**2)**0.5
        self.sd3 = ((self.p1.y - self.p3.y)**2 + (self.p1.x - self.p3.x)**2)**0.5
        return round(self.sd1+self.sd2+self.sd3, 4)
    
    def __str__(self):
        return f"{self.name} mit {self.p1} - {self.p2} - {self.p3}"

class Rechteck(Figur):
    def __init__ (self, pkt1, pkt2):
        super().__init__("Rechteck")
        self.p1 = pkt1
        self.p2 = pkt2

    def Umfang(self):
        self.sr1 = abs(self.p2.y - self.p1.y)
        self.sr2 = abs(self.p2.x - self.p1.x)
        return round(2* (self.sr1+self.sr2), 4)
    
    def __str__(self):
        return f"{self.name} mit {self.p1} - {self.p2}"       


class Kreis(Figur):
    def __init__ (self, mittelpunkt, radius):
        super().__init__("Kreis")
        self.m = mittelpunkt
        self.r = radius

    def Umfang(self):
        return round(math.pi*2*self.r,4)
    
    def __str__(self):
        return f"{self.name} mit M={self.m} und r={self.r}"


class Polygon(Figur):
    def __init__(self, punkte):
        super().__init__("Polygon")
        self.punkte = punkte
    
    def Umfang(self):
        u = 0
        for i in range(len(self.punkte)):
            j = (i + 1) % len(self.punkte)
            u += math.sqrt((self.punkte[i].x - self.punkte[j].x)**2 + 
                           (self.punkte[i].y - self.punkte[j].y)**2)
        return round(u,4)
    
    def __str__(self):
        punkte_string = ' - '.join(str(punkt) for punkt in self.punkte)
        return f"{self.name} mit {punkte_string}"


A = Punkt(1,1)
B = Punkt(2,2)
C = Punkt(4,4)
D = Punkt(3,5)
E = Punkt(1,2)

'''
w = Dreieck(A,B,C)
print(w)
print(w.Umfang())
#'''

'''
x = Rechteck(A,B)
print(x)
print(x.Umfang())
#'''

'''
y = Kreis(C,2)
print(y)
print(y.Umfang())
#'''

'''
z = Polygon([A,B,C,D])
print(z)
print(z.Umfang())
#'''