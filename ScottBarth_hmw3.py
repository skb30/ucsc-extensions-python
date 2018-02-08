
# homework assignmnet 3 - Calculate Employee Pay

# define some constants to allow for change
BASE_HOURS = 40
OT_HOURS   = 60
OT_FACTOR  = 1.5


def calculatePay(rate, nhours):
    otHrs   = 0;
    otRate  = rate * OT_FACTOR
    dtRate  = 0;
    dtHrs   = 0;
    def wages(rate, regHrs, otHrs, otRate, otWages, dtHrs, dtRate, dtWages):
            paycheck = "Regular hours: " + str(regHrs) \
              + " at rate $: " \
              + str(rate) \
              + "\nRegular wages: $" \
              + str(basePay) \
              + " \nOvertime hours: " \
              + str(otHrs) \
              + " at rate: " \
              + str(otRate) \
              + "\nOvertime Wages: $" \
              + str(otWages) \
              + "\nDouble Time hours: "\
              + str(dtHrs) \
              + " Double Time rate: " \
              + str(dtRate) \
              + "\nDouble Time Wages: $" \
              + str(dtWages) \
              + "\n---------------------\n" \
              + "\nTotal Wages: $" \
              + str(basePay +otWages + dtWages ) \
              + "\n---------------------\n\n"

            return paycheck

    if nhours <= BASE_HOURS:
        basePay = rate * nhours
        paycheck = wages(rate, nhours, 0, otRate, 0, 0, dtRate, 0)

    # if we made it here we know that nhours must be greater than 40 so
    # lets check if nhours is less than or equal to 60
    elif nhours <= OT_HOURS:
        otHrs = nhours - BASE_HOURS
        basePay = BASE_HOURS * rate
        otWages = otRate * otHrs
        paycheck = wages(rate, BASE_HOURS, otHrs, otRate, otWages, 0, 0, 0)


    # if we made it here we know nhours is over 60 so lets
    # calculate overtime and double time pay
    else:

        basePay = BASE_HOURS * rate
        otHrs   = 20
        otWages = otHrs * otRate

        dtHrs = nhours - OT_HOURS
        dtRate = rate * 2
        dtWages = dtHrs * dtRate
        # and we know we have 40 hours at base pay

        paycheck = wages(rate, 40, otHrs, otRate, otWages, dtHrs, dtRate, dtWages)

    return paycheck

# main


# run tests
print(calculatePay(30,20))     # expected value: 600
print(calculatePay(15.50,50))  # expected value: 852.5
print(calculatePay(11,70.25))  # expected value: 995.5


# collect employee data from user
rate = float(input("Please enter employee's rate of pay: "))
nhours = float(input("Please enter number of hours worked: "))

# call function using user data
print(calculatePay(rate,nhours))
