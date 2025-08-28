#Example of invoking the def statement
x = 5
print('Hello')

def print_lyrics():
    print("I'm a lumberjack, and I'm okay")
    print("I sleep all night and I work all day")

print('yo')
x = x + 2
print(x)
print_lyrics()     # you need to call the def statement to invoke (call) the function


# PUTTING IN ARGUMENTS FOR THE FUNCTION
# MIN and MAX are examples of arguments

big = max('Hello world')   # Arguments have to be put in parentheses after function name (here 'max')
print(big)

# PARAMETERS
# A parameter in Python is a name you put inside the parentheses when you define a function.
# It acts like a placeholder for a value that you give to the function when you call it.

def greet(name):  # 'name' is a parameter
    print("Hello", name)

greet("Lebron")    # We replace the parameter 'name' with an actual value when invoking 


#Another example of a parameter

def greet(lang):            # 'lang' is the parameter or placeholder for language of greeting
    if lang == 'es':        # Assuming es is for espanol
        print('Hola')
    if lang == 'fr':
        print('Bonjour')    # Assuming fr is for french
    else:
        print('Hello')      # If neither fr or es, just print 'Hello' in english
    exit()

greet('fr')                 # When invoking the def, we can replace lang with 'es', 'fr', or anything else to produce results


# RETURN
# return in Python is used inside a function to give back a value to the place where the function was called.
# It ends the function and sends a result out.

def greet():               # Here, unlike the previous example, there is no parameter
    return "Hello"         # everytime you invoke greet(), it returns a value of "Hello"

print(greet(), "Glenn")    # Here we want to print greet() and since it returns "Hello", it will be "Hello" followed by name
print(greet(), "Sally")

#Another more complex and practical use of return 
def add(a, b):             # we have a parameter for def add() where it is (a, b)
    return a + b           # for this def, we return the function of (a, b) as a + b

print(add(4, 5))           # Instead of writing a + b and asisgning values, it becomes easier to use the def and just replace values

# RETURN also allows us to improve and use formulae without making it cumbersome

# when modifying the lang example:

def greet(lang):           
    if lang == 'es':       
        return 'Hola'     # No brackets for return (unlike print in the previous example)
    if lang == 'fr':
        return 'Bonjour'   
    else:
        return 'Hello'       

print(greet('es'), 'Glenn')   
exit()