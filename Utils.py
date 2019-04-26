from random import randrange, getrandbits, randint

def multMod(a, b, p):
    """
    a*b mod(P)
    """
    return (a*b)%p

def addMod(a, b, p):
    """
    a+b (mod P)
    """
    return (a+b)%p

def isPrime(n, k=128):
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

def findPrime3Mod4(n):
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
        c=isPrime(a)
    return a       