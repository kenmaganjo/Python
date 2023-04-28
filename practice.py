# initial_string = 'The lazy dog ran so fast it hit the wall.' 
# first_part = initial_string[:12]
# second_part = initial_string[13:24]
# third_part = initial_string[25:]
# print(first_part + '; ' + second_part + '; ' + third_part)

# “  JOHn  .“ to “john”

# name1 = 'JOHn .'
# name2 = name1[:4]
# print(name2.lower())

# Slice the below string to get you the resulting sentence:
# sentence_one = “The Dog Breed is German Shepherd” only display “Breed is German”

# sentence_one = 'The Dog Breed is German Shepherd'
# new_sentence1 = sentence_one[8:23]
# print(new_sentence1)   -------ans: Breed is German

# temp = 56.8926 
# num1 = int(temp)
# num1 = round(temp)
# print(num1)    --------ans: 57

# temp = 56.8926 
# num1 = round(temp, 2)
# print(num1) -------------ans: 56.89

# temp = '56.8926' ---------('' added to convert float into str)
# num1 = temp[:6] ----------(slicing to get 56.892(str))
# num1 = float(num1) --------(to convert str back to float)
# print(num1) ---------------ans: 56.892

# print(type(num1)) ----------ans: <class 'float'>

temp = '56.8926'
num1 = temp[2:3]
num2 = temp[3:4]
num3 = temp[4:]
new_num = num2 + num1 + num3
new_num = float(new_num)
print(new_num)
print(type(new_num))

