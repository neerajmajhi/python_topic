'''def cylinder_volume(height, radius):
    pi = 3.14159
    return height * pi * radius ** 2
cylinder_volume(10, 3)'''

# variable scope example

egg_count = 0
'''def buy_eggs(): 
    egg_count += 12''' # purchase a dozen eggs

#buy_eggs()    reason of error:This code causes an UnboundLocalError, because the variable egg_count in the first line has global scope. Note that it is not passed as an argument into the function, so the function assumes the egg_count being referred to is the global variable.

#In the last video, you saw that within a function, we can print a global variable's value successfully without an error. This worked because we were simply accessing the value of the variable. If we try to change or reassign this global variable, however, as we do in this code, we get an error. Python doesn't allow functions to modify variables that aren't in the function's scope.
#solution :
def buy_eggs(count):
    return count + 12  # purchase a dozen eggs

egg_count = buy_eggs(egg_count)



