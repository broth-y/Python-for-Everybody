# Using loops (WHILE and FOR)

# While is very similar to an if statement, if the condition is met, do this, if not then skip to the else
# but 'if' is for checking condition once, 'while' enables the loop

x = 5
while x > 0:         # while makes sure that, as long as x > 0, it will come back and execute this same function (print(x) and x = x - 1) for all combinations till the loop ends
    print(x)
    x = x - 1        # subtracting 1 from x gets you out of the loop (+ would make it an infinite loop)
print("Blastoff!")
print(x)             # residual value for x (=0) when all the possible (5,4,3,2,1) and print("Blastoff") is looped


# Example of an infinite loop

# n = 5
# while n > 0:
#     print("im a barbie girl")

# BREAK statement breaks you out of the loop
while True:
    line = input('> ')
    if line == 'done':
        break                  # this is sort of an infinte loop as no matter what you type, its always gonna ask you for an input
    print(line)                # but when you input 'done', then the break is initiated and goes to the next code (out of the loop)
print('Done!') 

# Using Continue

# Continue statements ends the current iteration and jumps to the top of the loop and starts the next iteration

while True:
    line = input('> ')
    if line[0] == '#':
        continue              # doesn't stop the iteration, but goes back and starts the next iteration without conti
    if line == 'done':
        break
    print(line)
print('Done!')