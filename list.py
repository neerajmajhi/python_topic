# a list of boys 
boys = ["rist", "jack", "hero", "alan", "meet", "bob", "katie", "jack", "kali" ]
#testing mutablity on index 3
boys[3] = "miss"
#list of selected candidates
selected = boys[:3]
print("selected candidates are: ", selected)
#list of eliminated candidates
eliminated = boys[3:]
print('eliminated candidates are:', eliminated)
#checking in and not in method
print('alan' in boys, 'alan' not in boys)
#checking another way of indexing
print(boys[-1])

month = 8
days_in_month = [31,28,31,30,31,30,31,31,30,31,30,31]

# use list indexing to determine the number of days in month
num_days = days_in_month[7]

print(num_days)

eclipse_dates = ['June 21, 2001', 'December 4, 2002', 'November 23, 2003',
                 'March 29, 2006', 'August 1, 2008', 'July 22, 2009',
                 'July 11, 2010', 'November 13, 2012', 'March 20, 2015',
                 'March 9, 2016']
                 
                 
# TODO: Modify this line so it prints the last three elements of the list
print(eclipse_dates[-3 :])

#join method
left = ['i hate', 'world']
print(" ".join(left))
#append method
left.append('like')
print(left)