# rad * (180/pi) = deg
import math

def rad_to_deg(radians):
    degree = radians * (180 / math.pi)
    degree = round(degree, 3)
    return degree

def deg_to_rad(degree):
    radians = degree * math.pi / 180
    return radians

print(rad_to_deg(1))
print(deg_to_rad(57.3))