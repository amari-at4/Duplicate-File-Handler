# read animals.txt
# and write animals_new.txt
file = open('animals.txt', 'r')
new_file = open('animals_new.txt', 'w')
new_file.write(" ".join([line.rstrip('\n') for line in file]))
file.close()
new_file.close()
