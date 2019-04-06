from random import randrange, getrandbits, randint

class EllipticCourve:
    """
    Elliptic courve object
    y^2 = x^3 + Ax + B
    Modulo P
    """
    P = 0
    A = 0
    B = 0
    X = 0
    Y = 0
    Delta = 0

    def __init__(self, bits=256):
        p = self.findPrime3Mod4(bits)
        self.P = p
        delta = 0
        while delta == 0 :
            a = randint(1,10)
            b = randint(1,10)
            delta = 4*a**3 + 27*b**2
        self.A = a
        self.B = b
        self.Delta = delta
        print("krzywa to y^2 = x^3 + "+ str(self.A) + "x + "+str(self.B))

        while True :
            x = randrange(1,self.P)
            y2 = self.addMod(self.addMod(pow(x,3,self.P), self.multMod(a,x)), b)
            if (pow(y2,(p-1)//2, p))==1 :
                break
        self.X = x
        y = pow(y2,((self.P+1)//4),self.P)      
        self.Y = y
        print("X1 = " + str(x) + " Y1 = " + str(y))   


    def multMod(self, a, b):
        """
        a*b mod(P)
        """
        return (a*b)%self.P

    def addMod(self, a, b):
        """
        a+b (mod P)
        """
        return (a+b)%self.P


    def isPrime(self, n, k=128):
        """
        Miller-Rabin algorithm implementation
        Tests if number is prime
            Args:
                n - (int) number to test
                k - (int) prob(`n` is prime) <= 2**(-`k`)
            return True if n is prime
        """
        #for now, no need to check if even or if in (1,2)
        #becouse we are using it for only large numbers with lsb set to 1
        d = n - 1
        s = 0
        while d % 2 == 0:
            d //= 2
            s += 1
        
        for _ in range(k):
            a = randrange(2, n-2)
            x = pow(a,d,n)
            if x==1 or x==n-1:
                continue
            for _ in range(s-1):
                x = pow(x,2,n)
                if x==1:
                    return False
            if x!=n-1:
                return False
        return True

            

    def findPrime3Mod4(self, n):
        """
        looging for n bit prime that is 3 mod(4)
        n - nuber of bits in primme
        """   
        c=False
        while c==False:
            length = n
            a = getrandbits(length-2)
            a|=(1<<length-2-1)
            a=(a*4)+3
            c=self.isPrime(a)
        return a
