# For assignment 2.3, we have to write a prompt the user for hours and rate per hour to compute gross pay.
# We have to use input to read a string (setting a header) and float to convert the string to a  (for each different scenario). This is a must
# because input always returns a string and we need a number to do arithmetic.
# We have to use the print function to produce the output.
# We have to use the variable names hours and rate to store the user input.
# We have to use the variable pay to store the computed gross pay.
# This is to create a program that computes gross pay - including input (hours and rate) and output (pay).

hrs = input("Enter hours:") # Similar to creating input for hours like a website
rate = input("Enter rate:") # Similar to creating input for rate like a website
pay = float(hrs)*float(rate) # We set condition that converts the input string (word) into a decimal number (float) and multiply hours and rate to get pay
print("Pay:", pay)


# Practice using similar input function to float function to convert string to number with a financial example
# Developing a program to compute EV * EBITDA Muktiple for DCF valuation

ev = input("Enterprise Value:")
ebitda = input("EBIDTA:")
mult = float(ev)*float(ebitda)
print("EV/EBITDA Multiple:", mult)
