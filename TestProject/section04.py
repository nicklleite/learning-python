# #############################################################################
# Coding challenge part 4
#
# - Create a BMI calculator, BMI which stands for Body Mass Index can be
#   calculated using the formula:
#
#   BMI = (weight in Kg)/(Height in Meters)^2.
#
# - Write python code which can accept the weight and height of a person and
#   calculate his BMI.
#
#   Note: Make sure to use a function which accepts the height and weight
#   values and returns the BMI value.
# #############################################################################

def calc_bmi(w, h):
    return w / (h ** 2)


weight = float(input("Enter your weight (Kg): "))
height = float(input("Enter your height (m): "))
result = calc_bmi(weight, height)
print("BMI: ", result)
