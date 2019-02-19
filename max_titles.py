from characters import characters

# Who has the most titles?

# let's assume that we have seen no titles yet
most_titles = 0
person_with_most_titles = ''

# visit each character and see if they have more than 'most_titles'
for person in characters:
    num_titles = len(person['titles'])
    if num_titles  > most_titles:
            most_titles = num_titles
            # person_with_most_titles = person['name']

# if so , save that new value to 'most_titles'
# if not, ignore them

#print out the names of each person with the same number of titles as 'most_titles'
for person in characters:
    num_titles = len(person['titles'])
    if num_titles == most_titles:
        print("%s has %d titles" % (person['name'],most_titles))


print("nope that's it")









# # Who has the most titles?

# # let's assume that we have seen no titles yet
# most_titles = []
# for char in characters:
#     length = len(char['titles'])
#     most_titles.append(length)
#     if len(char['titles']) == max(most_titles):
#         print(char['name'])
# print(max(most_titles))
