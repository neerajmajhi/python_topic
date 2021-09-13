#example of the dictionary
#Result printing message
print('Result of this Examination')
results = {'ajay':85, 'kajal':74, 'anna':96, 'aarti':55, 'ramesh':67}
print(results)
#topper calculation
topper = max(results, key=results.get)
print("topper of this exam is: ", topper)

#another example for storing more than one properties
print('students Report card')            #printing the heading
report_card = {'rohan': {'hindi': 85,    # different subjects marks for student rohan 
                        'english':78,
                        'sanskrit':74,
                        'mathematics':78,
                        'science':78},
               'Aadi': {'hindi': 54,
                        'english':84,
                        'sanskrit':66,
                        'mathematics':73,
                        'science':71},
                'sneha': {'hindi': 96,
                        'english':56,
                        'sanskrit':88,
                        'mathematics':63,
                        'science':91},
                      
                        }
print(report_card['sneha'])  
                      
elements = {'hydrogen': {'number': 1, 'weight': 1.00794, 'symbol': 'H', 'is_noble_gas': False},
            'helium': {'number': 2, 'weight': 4.002602, 'symbol': 'He','is_noble_gas': True}}

print(elements['hydrogen']['is_noble_gas'])
print(elements['helium']['is_noble_gas'])
# todo: Add an 'is_noble_gas' entry to the hydrogen and helium dictionaries
# hint: helium is a noble gas, hydrogen isn't
#quiz 1
a = [1, 2, 3]
b = a
c = [1, 2, 3]

print(a == b)
print(a is b)
print(a == c)
print(a is c)