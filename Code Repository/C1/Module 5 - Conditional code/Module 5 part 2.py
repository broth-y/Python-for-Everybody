# Basic if and else statement

x = 4

if x > 2:
    print('More')
else:
    print('Less')
print('All done')


# usage of elif to accomodate multiple if statements (using 'else' alone only allows for two conditions)

def new_shit():  # a bit early, but used the def function to create this code subset called 'new_shit'
    x = 9
    if x < 2:
        print('less than 2')
    elif x < 10:             # elif allows us to add another condition (same indent level as 'if' and 'else')
        print('less than 10')
    elif x in range(2,10):   # added anothr elif condition using a range function (always use 'x in range' for range conditions)
        print('between 2 and 10')
    else:
        print('smashed it all')
    print('All done')

new_shit()  # after defining this entire if, else, elif under 'new_shit', just running 'new_shit' will produce the results of the code


# Using if and elif but ignoring else
x = 5
if x < 2:
    print('small')
elif x < 10:
    print('medium')  # if there is no else, then there is no condition that lands on something if other conditions fail as seen in the previous exmaple
print('All done')

# using 'try' and 'except' as insurance for possible tracebacks

# astr ='Hello Bob'
# istr = int(astr)
# print('First', istr)
# astr = '123'
# istr = int(astr)
# print('Second', istr)

# here we have a traceback as it is not possible to convert 'Hello Bob' into an integer (wrong even with an input() )
# so to correct or add protection to this, we use try and except

astr = 'Hello Bob'
try:
    istr = int(astr)  #This is the line for which we need insurance as it seeks to convert string into integer (not possible)
except:
    istr = -1    #If 'Hello Bob' fails (100% of that) instead of the traceback, istr will be == -1
print('First', istr)
astr = '123'
try:
    istr = int(astr)
except:
    istr = -1   #even thought this will work as '123' can be converted to integer, we still need the except line as insurance
print('Second', istr)

#another example of try and except using input function (header) to read a string and convert it to an integer

rawstr = input('Enter a number:')  #input function to read a string (setting a header for user to add a number)
try:
    ival = int(rawstr)  #try to convert the input string into an integer
except:
    ival = -1          #if it fails, set ival to -1 (supposr user enters a word instead of a number - forty two and not 42)

if ival > 0:
    print('Nice Work')
else:
    print('Not a number')

