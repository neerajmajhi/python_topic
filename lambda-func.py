# You can use lambda expressions to create anonymous functions. That is, functions that don’t have a name. 
# They are helpful for creating quick functions that aren’t needed later in your code. 
# This can be especially useful for higher order functions, or functions that take in other functions as arguments.

multiply = lambda x, y: x * y #anonymous fumction
multiply(4, 7)

#with lambda function
numbers = [
              [34, 63, 88, 71, 29],
              [90, 78, 51, 27, 45],
              [63, 37, 85, 46, 22],
              [51, 22, 34, 11, 18]
           ]

averages = list(map(lambda x: sum(x) / len(x), numbers))
print(averages)

#without it
numbers = [
              [34, 63, 88, 71, 29],
              [90, 78, 51, 27, 45],
              [63, 37, 85, 46, 22],
              [51, 22, 34, 11, 18]
           ]

def mean(num_list):
    return sum(num_list) / len(num_list)

averages = list(map(mean, numbers))
print(averages)

