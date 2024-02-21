# defining a function that takes an input of weight and height
# as integers and outputs BMI as an integer

# BMI is defined as the weight of an individual divided by their
# height squared

def bmi(weight, height):
    result = weight / (height * height)
    return result