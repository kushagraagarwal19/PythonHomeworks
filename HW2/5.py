johnDays = int(input("Please enter the number of days John has worked"))
johnHours = int(input("Please enter the number of hours John has worked"))
johnMinutes = int(input("Please enter the number of minutes John has worked"))

billDays = int(input("Please enter the number of days bill has worked"))
billHours = int(input("Please enter the number of hours bill has worked"))
billMinutes = int(input("Please enter the number of minutes bill has worked"))

totalMinutes = johnMinutes + billMinutes
carryForwardHours = totalMinutes//60
totalMinutes = totalMinutes%60

totalHours = johnHours+billHours+carryForwardHours
carryForwardDays = totalHours//24
totalHours = totalHours%24

totalDays = carryForwardDays+johnDays+billDays

print("The total time both of them worked together is: {} days, {} hours and {} minutes.".format(str(totalDays), str(totalHours), str(totalMinutes)))