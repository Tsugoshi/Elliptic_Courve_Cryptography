from random import randrange, getrandbits, randint
from Utils import addMod, multMod, findPrime3Mod4
from Point import Point
import cypari2 as cp

class EllipticCourve:
    """
    Elliptic courve object
    y^2 = x^3 + Ax + B
    Modulo P
    """
    # P = 0
    # A = 0
    # B = 0
    # X = 0
    # Y = 0
    # Delta = 0

    def __init__(self, bits=256):
        p = findPrime3Mod4(bits)
        self.P = p
        delta = 0
        while delta == 0 :
            a = randint(1,10)
            b = randint(1,10)
            delta = 4*(a**3) + 27*(b**2)
        self.A = a
        self.B = b
        self.Delta = delta
        self.Point = self.FindPointOnCourve()

    def FindPointOnCourve(self):
        while True :
            x = randrange(1,self.P)
            y2 = addMod(
                addMod( pow(x,3,self.P), multMod(self.A,x,self.P), self.P)
                ,self.B,self.P
                )
            if (pow(y2,(self.P-1)//2, self.P))==1 :
                break
        y = pow(y2,((self.P+1)//4),self.P)
        # if pow(y,2,self.P)==y2:
        #     print("Działa")      
        point = Point(x,y,self)
        return point

    def __str__(self):
        return ("y^2 = x^3 + "+ str(self.A) + "x + "+str(self.B)+ " " + "mod: "+str(self.P))
