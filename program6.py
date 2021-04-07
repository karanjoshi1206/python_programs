# By Karan joshi
# Program6: Create a function that take angle in radius and returns the angle in degree rounded to one decimal place

def angle_convert(radian_angle):
    converted_angle = radian_angle*(180/3.14)
    return round(converted_angle, 1)


print(angle_convert(1))
