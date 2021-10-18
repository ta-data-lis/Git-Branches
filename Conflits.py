from math import pi, pow


r = float(input ("Input the radius of the circle : "))


#  Area of the circle 
A = pi * pow(r,2)

print ("The area of the circle with radius " + str(r) + " is: " + A)


# Volume of the Sphere
V = 3/4 * pi * pow(r,3)

print("The volume of the sphere is: ", V)

