
test_var = 7

print(type(test_var))

test_var = 7.00

print(type(test_var))

sentence = 'I\'m learning python for the very first time this morning! We\'re having a great time.'

print(sentence)

print(sentence.upper())

new_sentence = sentence.split('!')[0]

print(new_sentence)

test_list = [9, 2, 7]

print(test_list[0])

test_list[2] = 4

print(test_list)

test_tuple = ('first', 'second', 'third', 'hello')

print(test_tuple[2])

if 'hello' in test_tuple:
    print('Passed')

test_dict = {
    "name": "Rakib",
    "Python_Skill": 3,
    "hadCoffee": "No",
}

print(test_dict)
test_dict['Python_Skill'] = 4

print(test_dict['name'])
print(test_dict)

test_dict['languages'] = ('Java', 'Javascript', 'C#')
print(test_dict)

fav_foods = {'Burgers', 'Loaded Fries', 'Fried Chicken'}

print(fav_foods)

print(f'There are {len(fav_foods)} items in my set')
