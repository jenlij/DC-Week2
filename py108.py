# Reading and writing files!

# Reading a file.
# Use the built-in `open` function

hello_file = open('hello.txt')
file_contents = hello_file.read()
print file_contents

# What if it doesn't exit?
boo_error_file = open('no_file_here_buddy.txt')
# (Error will print out)


# Reading line by line
swift = open('swift.txt')
swift_lines = swift.readlines()

for i in (range(len(swift_lines))):
  print "Line %d: %s" % (i+1, swift_lines[i])

# Writing to a new file.
# You can't use the same syntax.
# You need to tell python that you want to write.
# Here's the equivalent:
hello_file = open('hello.txt', 'r') # 'r' is for read

hello_file = open('hello.txt', 'w') # 'w' is for write (OVERWRITES once closed and opened again)
hello_file.write('hey!')
hello_file.write('hey you!')
hello_file.write('over here!')
hello_file.write('do you want a chik fil a cookie?')

hello_file.close()

# These are called "file modes"

# Writing to (appending to) a new file.
hello_file = open('hello.txt', 'a') # 'a' is for append




# Saving more complex stuff
# you need to write it as "binary"
# and use the pickle module

import pickle
silly = {
  'person': {
    'name': 'jethro',
    'age': 1000,
    'number_of_cats': 22
  },
  'cat': {
    'name': 'vin disel',
    'age': 11
  }
}
silly_file = open('silly.dat', "wb")
pickle.dump(silly, silly_file)
silly_file.close()
# to read it back out
file_of_silliness = open('silly.dat', 'rb')
silliness = pickle.load(file_of_silliness)
