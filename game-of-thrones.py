from characters import characters
import requests  # makes API requests (this is a third-party module)
import json  # convert the API data into python dictionaries and arrays
import time  # module for working with timestamps


# character_set = set(sorted(characters))
# print(character_set)
# print(len(characters))
# jon_snow = {"url":"https://anapioficeandfire.com/api/characters/583","name":"Jon Snow","gender":"Male","culture":"Northmen","born":"In 283 AC","died":"","titles":["Lord Commander of the Night's Watch"],"aliases":["Lord Snow","Ned Stark's Bastard","The Snow of Winterfell","The Crow-Come-Over","The 998th Lord Commander of the Night's Watch","The Bastard of Winterfell","The Black Bastard of the Wall","Lord Crow"],"father":"","mother":"","spouse":"","allegiances":["https://anapioficeandfire.com/api/houses/362"],"books":["https://anapioficeandfire.com/api/books/5"],"povBooks":["https://anapioficeandfire.com/api/books/1","https://anapioficeandfire.com/api/books/2","https://anapioficeandfire.com/api/books/3","https://anapioficeandfire.com/api/books/8"],"tvSeries":["Season 1","Season 2","Season 3","Season 4","Season 5","Season 6"],"playedBy":["Kit Harington"]}

# # print out the key names individually
# # for k in jon_snow:
# #     print(k)

# # print out just the values
# # for k in jon_snow:
# #     print(jon_snow[k])

# # print both thcode  the value
# for k in jon_snow:
#     print("%s: %s" % (k, jon_snow[k]))

# How many characters names start with "A"?
# print(characters['name'])

count = 0
for char in characters:
    if char['name'][0] == 'A':
        count += 1
        print("%s ,  %d " % (char['name'], count))
print(count)  # count of names starting with 'A'

# How many characters names start with "Z"?
count2 = 0
for char in characters:
    if char['name'][0] == 'Z':
        count2 += 1
        print("%s ,  %d " % (char['name'], count2))
print(count2)  # count of names starting with 'Z'


# How many characters are dead?
count3 = 0
for char in characters:
    if char['died'] != '':
        count3 += 1
print("%d characters died" % count3)

# Who has the most titles?

# let's assume that we have seen no titles yet
most_titles = []
for char in characters:
    length = len(char['titles'])
    most_titles.append(length)
    if len(char['titles']) == max(most_titles):
        print(char['name'])
print(max(most_titles))







# How many are Valyrian?
count4 = 0
for char in characters:
    if char['culture'] == 'Valyrian':
        count4 += 1
print("%d Valyrians" % count4)


# What actor plays "Hot Pie" (and don't use IMDB)?
for char in characters:
    if char['name'] == 'Hot Pie':
        print(char['playedBy'])


# How many characters are *not* in the tv show?
count5 = 0
for char in characters:
    if char['playedBy'] == [""]:
        print(char['name'])
        count5 += 1
print("%d characters are not in the tv show" % count5)

# Produce a list characters with the last name "Targaryen"
# count6 = 0

# for char in characters:
#     name_list = char['name'].split()
#     last_name = name_list[1]
#     if last_name == 'Targaryen':
#         count6 += 1
# print("%d Targaryens" % count6)

# Create a histogram of the houses (it's the "allegiances" key)


# count the nunber of people who are part of a house
def make_house_histogram(character_list):
    histogram = {}

    # do the thing!
    # loop through all the characters
    for person in character_list:

        # what do i check for each person?
        allegiances = person['allegiances']
        # allegiances is a list of URLs
        for house in allegiances:
            # do something with that house
            if house in histogram:
                histogram[house] = histogram[house] + 1
            else:
                histogram[house] = 1

    return histogram


def pretty_print_histogram(histogram):
    for house in histogram:
        print('%s has %d members' % (house, histogram[house]))


def translate_address_to_house_name(URL):
    house_name = ''
    r = requests.get(URL)
    house_info = r.json()
    house_name = house_info['name']
    return house_name


def convert_to_nice_names(histogram):
    nice_histogram = {}
    for url in histogram:
        house_name = translate_address_to_house_name(url)
        nice_histogram[house_name] = histogram[url]
        time.sleep(0.1)

    return nice_histogram


# print(translate_address_to_house_name('https://www.anapioficeandfire.com/api/books/2'))

ugly_histogram = make_house_histogram(characters)
pretty_histogram = convert_to_nice_names(ugly_histogram)
pretty_print_histogram(pretty_histogram)


# pretty_print_histogram(make_house_histogram(characters))

# print(make_house_histogram(characters))
