#3.1 Write a program to prompt the user for hours and rate per hour using input to compute gross pay. 
# Pay the hourly rate for the hours up to 40 and 1.5 times the hourly rate for all hours worked above 40 hours. 
# Use 45 hours and a rate of 10.50 per hour to test the program (the pay should be 498.75). 
# You should use input to read a string and float() to convert the string to a number. 
# not worry about error checking the user input - assume the user types numbers properly.

hrs = input("Enter Hours: ")
rate = input("Enter Rate per hour: ")
try:
    h = float(hrs)                        # We convert the input string (word) into a decimal number (float) for easier arithmetic
    r = float(rate)                       # We convert the input string (word) into a decimal number (float) for easier arithmetic
except:
    print("Please enter a numeric value") # Insurance in case user enters a word instead of a number
if h <= 40:                               #condition: if hours worked is less than or equal to 40
    pay = h * r                           #pay is hours worked multiplied by rate per hour (no overtime)
else:                                     #condition: if hours worked is greater than 40
    opay = 40 * r + (h - 40) * r * 1.5    #pay = regular pay for 40 hours + overtime pay for hours above 40 at 1.5 times the rate
                                          # (h - 40) gives the number of overtime hours worked*1.5*r gives the overtime pay rate
print(opay)


#better way of writing the above problem

hrs = input("Enter Hours: ")
rate = input("Enter Rate per hour: ")
try:
    h = float(hrs)                        
    r = float(rate)       
except:
    print("Please enter a numeric value")

if h > 40:                    #condition: if hours worked is greater than 40 (changed from before)
    regpay = h*r
    otpay = (h-40)*r*0.5        # 0.5 because it is 1.5 times the rate but we have already paid r for all hours worked (h*r) (1.5r - r = 0.5r) where r = 1
    ovpay = regpay + otpay      # we add regular pay and overtime pay to get overall pay instead of just pay
else:
    pay = h*r
print("Pay:", ovpay)  # ovpay is overtime pay (for hours above 40)


# Write a program to prompt for a score between 0.0 and 1.0. If the score is out of range, print an error. If the score is between 0.0 and 1.0, print a grade using the following table:
# Score Grade
# >= 0.9 A
# >= 0.8 B
# >= 0.7 C
# >= 0.6 D
# < 0.6 F
# # If the user enters a value out of range, print a suitable error message and exit. For the test, enter a score of 0.85.

# 1. Read input and convert to float
score = input("Enter score: ")
try:                                    # if user enters a word instead of a number, then we need insurance (here an error msg)
    score = float(score)                # converting string to a decimal (float) number
except ValueError:
    print("Error: that’s not a number.")    # excpet (if user doesnt enter a number of "Enter Score" input) to this msg
    exit()

# 2. Check valid range
if score < 0.0 or score > 1.0:          # error message if score entered by user is beyond the scoring grade rane (0.0 - 1.0)
    print("Error: score out of range.")
    exit()

# 3. Decide grade
if score >= 0.9:
    grade = "A"
elif score >= 0.8:
    grade = "B"
elif score >= 0.7:
    grade = "C"
elif score >= 0.6:
    grade = "D"
else:
    grade = "F"                        # instead of setting range, we can just write the conditions as it assumes range on the >,>= comparison metrics

# 4. Print result
print("Grade:", grade)


# SAME ASSIGNMENT QUESTION BUT WITH ADDITIONAL REMARKS (PRINT) FOR EACH GRADE

score = input("Enter score between 0.0 and 1.0: ")
try:
    score = float(score)
except:
    print("Please enter numerical value between 0.0 and 1.0")
    exit()      # exit() should be within the indent of the sub code for it to end if initial condition is not meant

if score < 0.0 or score > 1.0:
    print("Please enter a value between 0.0 and 1.0")
    exit()      # same for this

if score >= 0.9:
    print('A')
    print('Good Job!!')
elif score >= 0.8:
    print('B')
    print('Good work but can do better!')
elif score >= 0.7:
    print('C')
    print('I like the attempt but need to work more.')
elif score >=0.6:
    print('D')
    print('Remedial classes will do you good.')
else:
    print('F')
    print('Inform your parents to meet me.')

print('Please think hard about my remarks.')
exit()         # To prevent a loop