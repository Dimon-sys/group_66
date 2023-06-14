#my_file = open('file.txt', 'w')
#my_file.write('Hello!')
#my_file.close()

my_file = open('file.txt', 'r')
my_text = my_file.read()
print(my_text)
my_file.close()