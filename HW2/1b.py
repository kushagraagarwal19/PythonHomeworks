import sys

pounds = input("Please enter weight in pounds:")
try:
    pounds = float(pounds)
except:
    print("Please enter numerical value of pounds")
    sys.exit()

inches = input("Please enter height in inches:")
try:
    inches = float(inches)
except:
    print("Please enter numerical value of height")
    sys.exit()

kilogram = pounds * 0.453592
print (kilogram)
meters = inches * 0.0254
print (meters)

BMI = str(kilogram/(meters*meters))
print("BMI is: {}".format(BMI))