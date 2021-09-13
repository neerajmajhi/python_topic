# example 1
for i in range(0,5):
    print('hi')
#example 2
cities = ['new york city', 'mountain view', 'chicago', 'los angeles']
for city in cities:
    print(city)
print("Done!")
# example 3:
sentence = ["the", "quick", "brown", "fox", "jumped", "over", "the", "lazy", "dog"]

# Write a for loop to print out each word in the sentence list, one word per line
for i in sentence:
    print(i)
#example 4:

for i in range(5,35,5):
    print(i)
#example 5: 
book_title =  ['great', 'expectations','the', 'adventures', 'of', 'sherlock','holmes','the','great','gasby','hamlet','adventures','of','huckleberry','fin']
word_counter = {}
for word in book_title:
    if word not in word_counter:
        word_counter[word] = 1   
        print(word_counter)
    else:
        word_counter[word] += 1
        print(word_counter)


