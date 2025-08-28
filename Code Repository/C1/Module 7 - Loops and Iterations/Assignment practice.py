tot = 0
pot = (5,4,3,2,1)
for i in pot:
    tot = tot + 1
    print(tot, i)
print('After', tot)


zork = 0 
things = (9, 41, 12, 3, 74, 15)
for thing in things:
    zork = zork + thing
    print(thing, zork)
print('After', zork)

smallest_so_far = -1
for the_num in (9, 41, 12, 3, 74, 15):
    if the_num < smallest_so_far:
        smallest_so_far = the_num
print(smallest_so_far)


n = 0
while n>0:
    print('lather')
print('dry off')

# Write a program that repeatedly prompts a user for integer numbers until the user enters 'done'.
# Once 'done' is entered, print out the largest and smallest of the numbers. 
# If the user enters anything other than a valid number catch it with a try/except and put out an appropriate message and ignore the number.
# Enter 7, 2, bob, 10, and 4 and match the output below.

smallest = None                              # always set this condition for finding min or max
largest = None
while True:                                  # if you want to create an infinite loop as they have asked and dont have x = 5, if x > 0 then print, just type 'While True' to trigger infinite loop
    inp = input("Enter Value:")              # we need to create an input for users to write the given integers value
    if inp == 'done':                        # if user inputs "done", then the loop breaks
        break 
    try:                                     # Insurance: if user inputs anything other than integers we go to the except
        num = int(inp)                       # create new sub to convert your input (inp) into an integer (int(num) where num is the new user input)
    except:
        print("Invalid input")               # if user input is anything non-integer then it returns this printed message
        continue
    if smallest is None or num < smallest:   # if smallest is none or num (input) is lesser than smallest number, then the smallest number is the new input (we merge equal to none and the lesser than smallest with an 'or' function)
        smallest = num
    if largest is None or num > largest:     # same here for largest
        largest = num
print("Maximum is", largest)                # we only print the maximum is value ands minimum is value as the desired output suggests
print("Minimum is", smallest)

# other printed message would be due to except function where the user may have input (num) a non integer value
