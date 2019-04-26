import EllipticCourve as ec


x = ec.EllipticCourve(256)
print(str(x))
p1 = x.Point
print(str(p1))
p2 = x.FindPointOnCourve()
print(str(p2))
print("2*p1 = "+str(p1+p1))
print("p1 + p2 = " + str(p1+p2))
print("3 * p1 = "+ str(p1.Multiply(6)))
print("p1+p1+p1 = " + str(p1+p1+p1+p1+p1+p1))

