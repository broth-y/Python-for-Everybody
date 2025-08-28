# INDEFINITE LOOPS EXAMPLE USING LOGICAL CONDITIONS (WHERE, CONTINUE, BREAK) FROM PREVIOUS LESSON
# n = 22
# while n > 0:
#     print(n)
#     n = n + 11
#     if n == 55:
#         continue
#     if n > 333:
#         break
# print("Loop done")


# DEFINITE LOOPS - FINITE

# here we use the 'for' construct

# a simple definite loop example

for i in [6,5,4,3,2,1]:      # for i within the range [6-1] this range is definite
    print(i)
print("Blastoff")

friends = ['Joesph', 'Glenn', 'Sally']    # be careful here - just cause 'friend' and 'friends' are written here, python does NOT undertsand plurals
for friend in friends:                    # friend is just one of the defined strings within the defined range ['Joesph', 'Glenn', 'Sally']  
    print('Happy New Year:', friend)      # runs a loop first with joesph, then glenn and then sally
print('Done!')


dudes = ('John', 'Jones', 'Bones')
for i in dudes:                        # 'for' does this for us. It runs the definite loop for us if we define it clearly
    print("you are a junkie ", i)      # 'for' _____ 'in' defined range -----> print, return or whatever you wanyt from it
print("You aint the goat!")

