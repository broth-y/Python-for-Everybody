# Suppose we want to create a counter or output no. alongside the output to keep track

count = 0                              # zork is the output no. and base is 0 as we add +1 for each number we go down on the list
print('Before', count)                 # Almost like a header ('Before 0')
things = (9, 41, 12, 3 , 74, 15)       # Doing what adi said and defining our range into things (so I dont need to type it again)
for thing in things:                   # 'for' function where 'thing' goes one by one down the range of 'things'
    count = count + 1                  # for each time you go down the range, the no. (zork) increases by 1
    print(count, thing)                # printing (no. of output, output from range)
print('After', count)


# Totalling up a series of values (sum)

count = 0
print('Before', count)
things = (9, 41, 12, 3, 75, 15)
for thing in things:
    count = count + 1
    print(count, thing)
total = sum(things)
print('Total:', total)
print('After', count)

# other way of doing thing but showing it as a cummulative value

sum = 0
print('Before', count)
things = (9, 41, 12, 3, 75, 15)
for thing in things:
    sum = sum + thing        # this is keeping 'sum' as the name for cummulative value
    print(thing, sum)        # instead of adding 1 to the count (this was to find the number as we go down), we add the 'thing' or range to find cummulative
print('After', sum)          # count serves as the calculation for finding cummulative total


#Finding averages in this loop (along with count and sum[cumm])

count = 0
sum = 0
print('Before', count, sum)
things = (9, 41, 12, 3, 75, 15)
for thing in things:
    count = count + 1                 # as we are finding the number
    sum = sum + thing                 # cummulative
    print(count, thing, sum)          # printing them in order - count(no.) then thing (individual entry from defined range) and then sum (cumm)
print('After', count, sum, sum/count) # instead of using len (things) to get average, I can just use count that I have gotten


# Filtering the range while keeping sum, count and average

count = 0
sum = 0
print('Before', count, sum)
things = (9, 41, 12, 3, 75, 15)
for thing in things:
    count = count + 1            
    sum = sum + thing               
    print(count, thing, sum)            
    if thing > 20:                       # create an if statement within the for statement as it deals with 'thing' in 'things'    
        print('Large Number', thing)     # so for whichever number (thing) within the list (things) is larger than 20, it would print (Large Number under it)
print('After', count, sum, sum/count)

# Searching and filtering using Boolean variable
  # this is mainly yes/no, true/false type variable

found = False                           # Initial assumption that list has no 3 and it is false
print('Before', found)
things = (9, 41, 12, 3, 75, 15)
for thing in things:
    if thing == 3:                       # we dont need an else function after if as this is Boolean
        found = True                     # since found = False, true is the only other option ---> it is understood
    print(found, thing)                  # as long as it is printed an the code has found a 3, then what was initially false, now become true
print('After', found) 


# Finding SMALLEST value in the list (check previous file for largest)

smallest_so_far =  None                 # How this differs from finding the largest number is that the smallest_so_far must be greater than all the numbers in the list
print('Before', smallest_so_far)        # We use None as the base as it assumes neither largest, base, or biggest 
things = (9, 41, 12, 3, 75, 15)
for thing in things:
    if smallest_so_far is None:         # so we assume that the start of the loop is that if smallest_so_far is none (note that 'is' is used and not '=')
        smallest_so_far = thing         # the first number in the list is the smallest so far and we go from there
    elif thing < smallest_so_far:       # else if number on list is lesser than smallest so far, then that becomes the new smallest so far
        smallest_so_far = thing        
    print(smallest_so_far, thing)
print('After', smallest_so_far)

# NOTES:
# 'for' loops are for definite loops and 'while' is used for indefinite (if it meets condition then it loops forever)
# For indefinite loops, you use break to skip the loop and move to the next code so that it doesnt go on forever (preceeded by if)
# 'if' such = such, then break -----> example of break
# 'continue' goes back to the top and starts the next from the start --> both 'for' and 'while' loops
# Dont use min and max for finding largest or smallest ----> use 'none' as the base
# 'is' and 'is not' are logical operators specifically for Boolean variables and 'None'

