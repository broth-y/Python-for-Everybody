# LOOKING FOR THE LARGEST/SMALLEST SET OF NUMBERS WITHIN A LOOP (FUNCTION WITHIN A LOOP)

# We are going to write a 'for' loop, but we are then going to set some initial values for certain variables
# after the loop ends (if definite then fine, but if indefinite then use break and continue), 
# we get the values we wanted to see from the loop initally

# this is the loop example we are using for this set

print('Before')                          # we get 'Before'
for thing in [9, 41, 12, 3, 74, 15]:     # defined loop as given range
    print(thing)                         # we print the loop after defining it using the 'for' and 'in'
print('After')                           # we also get 'after'

# we want to find the max value from this defined range from this loop

print('Before')
things = [9, 41, 12, 3, 74, 15]          # taking from the previous module, I defined my range under variable 'things'
for thing in things:                     # again, not plural but 'thing' in 'things' goes through each int within range, creating variable
    print(thing)                         # First get through the loop by printing it
print("Max:", max(things))              # be careful of indents - in main line, print the max(things) = max of your defined range
print("Min:", min(things))
print("Average:", int(sum(things)/len(things)))  # I also added in avreage and min as other things you want to find out after loop is finished
print('After')


# Better way to write this

largest_so_far = -1
print('Before', largest_so_far)
for the_num in [9, 41, 12, 3, 74, 15]:
    if the_num > largest_so_far:        # if_num is greater than the current largest so far (startin at -1)
        largest_so_far = the_num        # the new largest so far = to the number it just passed within the range
    print(largest_so_far, the_num)      # since we have used the 'for'____'in'_____ function for the range, it runs through a definite loop

print('After', largest_so_far)

# using 'none' as the base for largest_so_far

largest_so_far = None
print('Before', largest_so_far)
numbers = [9, 41, 12, 3, 74, 15]
for number in numbers:
    if largest_so_far is None:          # if followed by is (None)
        largest_so_far = number         # Initially if largest so far is none, then the initial number in the list is the new largest so far and we work from there
    elif number > largest_so_far:       # else if next number is greater than the current largest so far, then the new largest is the next number (goes down the loop to check)
        largest_so_far = number
    print(largest_so_far, number)       # we print this to get the numbers in the output
print('After', largest_so_far)
