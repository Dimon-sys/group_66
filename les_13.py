first_var = 22
second_var = 3.14

print(first_var + second_var)
print(first_var - second_var)
print(first_var * second_var)
print(first_var / second_var)

print(type(first_var), type(second_var))

third_var = "Привет, мир!"
print(third_var)
sub_string_hello = third_var[0:6]
sub_string_word = third_var[8:11]
print("M" + sub_string_word[1:] + ', ' + 'п' + sub_string_hello[1:])