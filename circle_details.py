#circule area...
import math
radius = float(input("Enter the radius of the circle : "))

def circle_area(r) : 
    return math.pi*pow(r,2)

print(f"Area of the circle is : {circle_area(radius)}")