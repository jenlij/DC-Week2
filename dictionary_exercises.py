#Ex 1 fixed keys
phonebook_dict = {
  'Alice': '703-493-1834',
  'Bob': '857-384-1234',
  'Elizabeth': '484-584-2923'
}
#print phonebook_dict['Elizabeth']
phonebook_dict.update({'Kareem': '938-489-1234'})
#print phonebook_dict
del phonebook_dict['Alice']
#print phonebook_dict
phonebook_dict['Bob'] = '968-345-2345'
#print phonebook_dict.items()

#Ex 2 dynamic keys
ramit = {
  'name': 'Ramit',
  'email': 'ramit@gmail.com',
  'interests': ['movies', 'tennis'],
  'friends': [
    {
      'name': 'Jasmine',
      'email': 'jasmine@yahoo.com',
      'interests': ['photography', 'tennis']
    },
    {
      'name': 'Jan',
      'email': 'jan@hotmail.com',
      'interests': ['movies', 'tv']
    }
  ]
}

#print ramit['email']
#print ramit['interests'][0]
# for dictionary in ramit['friends']:
#     if dictionary['name'] == 'Jasmine':
#         print dictionary['email']

# for dictionary in ramit['friends']:
#     if dictionary['name'] == 'Jan':
#         print dictionary['interests'][1]      


#Ex 3 letter summary dynamic keys
def letter_histogram(word):
    dictionary = {}
    for letter in word.lower():
        if letter in dictionary:
            #if letter in dictionary, value += 1
            dictionary[letter] = dictionary[letter] + 1 
        else: #if not, add letter to dictionary, set value to 1
            dictionary.update({letter: 1})
    return dictionary        
print letter_histogram('Hello')
print letter_histogram("bananananana")        

#Ex 4 word summary dynamic keys
def word_histogram(sentence):
    word_dictionary = {}
    for word in sentence.lower().split():
        if word in word_dictionary:
            word_dictionary[word] = word_dictionary[word] + 1
        else:
            word_dictionary.update({word: 1})
    return word_dictionary            

print word_histogram("To be or not to be")


#Ex 5 Bonus Challenge Top 3 words or letters
import operator
print "START HERE"
def winners(histogram):
    sorted_hist = sorted(histogram.items(), key=operator.itemgetter(1), reverse=True)
    print sorted_hist
    length = len(sorted_hist)
    print length
    if length > 3:
        for i in range(3):
            print sorted_hist[i][0]
    else:
        for i in range(length):
            print sorted_hist[i][0] 
winners(letter_histogram("aaaaaabbbbccccccccccccd"))
winners(word_histogram("my my hello hello hello to"))

