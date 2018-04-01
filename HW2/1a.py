import sys

kilogram = input("Please enter weight in kilograms:")

try:
    kilogram = float(kilogram)
except:
    print("Please enter numerical value of weight")
    sys.exit()

meters = input("Please enter height in meters:")

try:
    meters = float(meters)
except:
    print("Please enter numerical value of height")
    sys.exit()

BMI = str(kilogram/(meters*meters))
print("BMI is: {}".format(BMI))