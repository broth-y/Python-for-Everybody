# Example of return with a parameter
def add(a, b, c):
    return a+b+c

print(add(4,5,6), "Dollars")  # print then the def as just putting def would not get any output

# Understanding print vs return using music lyrics
def met():
    return 'We Will We Will'          # return this and then print using the def

print(met(),"Rock You","By Queen")


def addtwo(a,b):
    added = a + b
    return a         # since we only return a for addtwo(a, b), we only get the value of a when printing x (=addtwo(a, b)).

x = addtwo(2,7)
print(x)


# 4.6 Write a program to prompt the user for hours and rate per hour using input to compute gross pay. 
# Pay should be the normal rate for hours up to 40 and time-and-a-half (1.5x) for the hourly rate for all hours worked above 40 hours. 
# Put the logic to do the computation of pay in a function called computepay() and use the function to do the computation. 
# The function should return a value. Use 45 hours and a rate of 10.50 per hour to test the program (the pay should be 498.75). 
# You should use input to read a string and float() to convert the string to a number.
# Do not worry about error checking the user input unless you want to - you can assume the user types numbers properly.
# Do not name your variable sum or use the sum() function.

def computepay(h, r):                          # defining our code called computepay(hours, rate):
    if h > 40:                                 # setting condition (if) hours worked > 40
        overtime = h - 40                      # if yes, the overtime is = hours worked overtime - 40 hours
        pay = (40 * r) + (overtime * r * 1.5)  # pay = normal rate of 40hrs*rate + overtime (=(h-40)*r*1.5)
    else:
        pay = h * r                            # if Hours worked is <=40, then it follows the normal formula of (40*rate)
    return pay                                 # return pay for whatever condition it hits (be careful of indents)

hrs = input("Enter Hours:")                    # we now create the input for entering the values of both hrs and rate
rate = input("Enter Rate:")
try:
    h = float(hrs)                                 # converting string to float
    r = float(rate)
    pay = computepay(h,r)                      # always make a header to store values so I can just use 'pay' instead of computepay(h,r)

except:
    print("Please enter numerical value")

print("Pay", pay)                 # printing Pay: while calling/invoking the def that uses the conditional statement