# rad * (180/pi) = deg
import math

def rad_to_deg(radians):
    degree = radians * (180 / math.pi)
    degree = round(degree, 3)
    return degree

print(rad_to_deg(1))