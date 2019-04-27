class Point:
    """
    Class represents point on Elliptic Courve
    """

    def __init__(self,x,y,courve,neut=False ):
        self.X = x
        self.Y = y
        self.Courve = courve
        self.P = courve.P
        self.A = courve.A
        self.Neut = neut

    def __add__(self, other):

        if self.Neut :
            return other

        if other.Neut:
            return self

        if self.X != other.X:
            m = (other.Y - self.Y)*modinv((other.X-self.X), self.P)%self.P
            x = (pow(m,2,self.P) - self.X - other.X)%self.P
            y = (m * (self.X - x) - self.Y)%self.P
            return Point(x,y,self.Courve)

        if self.X == other.X and self.Y != other.Y:
            return Point(0,0,self.Courve,True)

        if self.X == other.X and self.Y == other.Y and self.Y !=0:
            m = (((3*pow(self.X, 2, self.P)) + self.A) * modinv(2*self.Y, self.P))%self.P
            x = (pow(m,2,self.P) - (2 * self.X)%self.P)%self.P
            y = ((m * (self.X - x))%self.P - self.Y)%self.P
            return Point(x,y,self.Courve)
            
        if self.X == other.X and self.Y == other.Y and self.Y ==0:
            return Point(0,0,self.Courve,True)

    def Multiply(self, n):
        """
        Adds points to itself n times using binary addition algorithm
        for n=2^256 it will only need 256 addition
        """
        bits = bin(n)[2:]
        Q = Point(0,0,self.Courve)
        for bit in bits :
            if bit == "1":
                Q+=Q
                Q+=self
            else :
                Q+=Q
        return Q



    def __str__(self):
        return "X= {} Y= {}".format(self.X, self.Y)
            

def extended_gcd(aa, bb):
    lastremainder, remainder = abs(aa), abs(bb)
    x, lastx, y, lasty = 0, 1, 1, 0
    while remainder:
        lastremainder, (quotient, remainder) = remainder, divmod(lastremainder, remainder)
        x, lastx = lastx - quotient*x, x
        y, lasty = lasty - quotient*y, y
    return lastremainder, lastx * (-1 if aa < 0 else 1), lasty * (-1 if bb < 0 else 1)
    
def modinv(a, m):
    g, x, y = extended_gcd(a, m)
    if g != 1:
        raise ValueError
    return x % m

