# STORE AND REUSE OF FUNCTIONS
# Store codes and functions under names for later use

def thing():
    print('Hello')
    print('Fun')          # anything within def___() must be sub indented always. This statement doesnt execute
                          # only typing thing() will execute it later, this is for defining it
thing()                   # we CALL the function here ----> prints 'Hello' and 'Fun' as dictated by its definintion code
print('Zip')
thing()                   # same thing here


# using 'max' and 'min' function
# similar to excel min/max function but also works on string variables

big = max('Hello world')    # big is the variable to find out the max word in the alphabet from 'Hello World' 
print(big)                  # Output of big would be 'w' as it is the latest letter in the alphabet scale

tiny = min('Hello world')
print(tiny)                 # min works similarly but since 'space' is the tiniest word here, it returns as space = empty


def minmax():               # Defining a min/max function example using integers
    big = max('4800','6500','4567')
    print(big)
    tiny = min('356789','67899', '7')
    print(tiny)
    exit()

minmax()                    # invokes (calls) for the results of the code (finding min/max and then printing said variable)

# TYPE CONVERSIONS 
print(float(99)/100)
i = 42
type(i)
f = float(i)
print(f)
type(f)
print(1+2*float(3)/4-5)  # Does multiplication first, then division and then addition

mult = 2*float(3)
div = 4-5

print(mult/div)


