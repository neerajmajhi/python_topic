''''try:
    num_each = cookies // people
    leftovers = cookies % people
except ZeroDivisionError:
    print("Oops, you entered 0 people will be attending.")
    print("Please enter a good number of people for a party.")

return(num_each, leftovers)