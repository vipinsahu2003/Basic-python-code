#  Write user input and append data to 'output.txt', then read all content

user_input = input("Enter some text to write to the file: ")

with open('output.txt', 'w') as file_write:
    file_write.write(user_input + '\n')

additional_data = "Appended line of text."
with open('output.txt', 'a') as file_append:
    file_append.write(additional_data + '\n')

with open('output.txt', 'r') as file_read:
    content = file_read.read()
    print("Final content of the file:")
    print(content)
