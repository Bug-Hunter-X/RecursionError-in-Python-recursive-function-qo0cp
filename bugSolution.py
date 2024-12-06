def my_function(x):
    if x > 1000: # Added check to prevent large recursion
        raise ValueError("Input too large for recursion")
    if x == 0:
        return 0
    else:
        return my_function(x - 1) + x

print(my_function(5))
print(my_function(1000)) 
#print(my_function(1001)) #this will produce ValueError