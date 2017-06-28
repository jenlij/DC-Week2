#1. Write a program that prompts the user to enter a file name, 
### reads the contents of the file and prints it to the screen.
def enter_filename():
    filename = raw_input("Please enter a file name: ")
    return filename

def open_read_print(filename):
    openme = open(filename)
    readme = openme.read()
    openme.close()
    print readme

def main1():
    userfile = enter_filename()
    open_read_print(userfile)

#main1()    

#2. Write a program that prompts the user to enter a file name, 
###then prompts the user to enter the contents of the file, and then saves the content to the file.
def collects_contents():
    contents = raw_input("Please enter your content to save: ")
    return contents

def writes_to_file(filename, contents):
    openfile = open(filename, 'w') 
    openfile.write(contents)
    openfile.close()

def main2():
    userfile = enter_filename()
    usercontent = collects_contents()
    writes_to_file(userfile, usercontent)
    print "Done"

#main2()

def main3():
    userfile = enter_filename()
    usercontent = collects_contents()
    writes_to_file(userfile, usercontent)
    open_read_print(userfile)
    print "I'm complete"

#main3()  



#3. Write a program that prompts the user to enter a file name, 
### then prints the letter histogram and the word histogram of the contents of the file.
def letter_hist(word):
    dictionary = {}
    for letter in word.lower():
        if letter in dictionary:
            #if letter in dictionary, value += 1
            dictionary[letter] = dictionary[letter] + 1 
        else: #if not, add letter to dictionary, set value to 1
            dictionary.update({letter: 1})
    return dictionary        

#Ex 4 word summary dynamic keys
def word_hist(sentence):
    word_dictionary = {}
    for word in sentence.lower().split():
        if word in word_dictionary:
            word_dictionary[word] = word_dictionary[word] + 1
        else:
            word_dictionary.update({word: 1})
    return word_dictionary            

def main4():
    userfile = enter_filename()
    openme = open(userfile)
    readme = openme.read()
    openme.close()
    
    print "letter histogram:"
    print letter_hist(readme)
    print "word histogram:"
    print word_hist(readme)

main4()    