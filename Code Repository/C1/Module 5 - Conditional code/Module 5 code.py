x = 5
if x == 5:
    print('Equal to 5')
if x > 4:
    print('Greater than or equal to 5')
if x < 6:
    print('Less than or equal to 6')
if x <= 5:
    print('Less than or equal to 5')
if x != 6:
    print('Not equal to 6')
print('All done')


# Second example of conditional execution (if and indents)

x = 5
print('Before 5')
if x == 5:
    print('Is 5')
    print('Is still 5')
    print('Third 5')
print('Afterwards 5')
print('Before 6')
if x == 6:  # This condition doesn't run and will skip to the next line after the indents as x = 5 (first line)
    print('Is 6')
    print('Is still 6')
    print('Third 6')
print('Afterwards 6')


# 3rd example of conditional execution (if, else and indents)

x = 5        # we set x = 5 for this conditional execution example
if x > 2:
    print('Bigger than 2')
    print('Still bigger')       # as x > 2 (=5), this condition runs and prints both lines as it is our instruction should it meet the condition
print('Done with 2')            # this line runs after the if block is done - look at indents

for i in range(5):              # variable is i and for is used to repeat the block of code 5 times (0,1,2,3,4),range(5) means 0 to 4
    print(i)
    if i > 2:                   # we add a condition that if i > 2, it will print the next line
        print('Bigger than 2')  # indent within an indent is called a nested block
    print('I am done with i')
print('All done')


# example of using the 'else' statement within conditional execution (simplifies multiple if statements

x = 4
if x > 2:
    print('Bigger than 2')
else:                      # else is indented at the same level as 'if' because it is the other side of the condition (not nested)
    print('2 or smaller')
print('All done')
exit()
 