def get_reverse(base_string):
    base_list = list(base_string)
    reverse = ""
    for i in range(len(base_list)):
        reverse += base_list[(len(base_list) - 1) - i]

    return reverse

word = input("Enter a word to get its reverse: ")
print(word + " -> " + get_reverse(word))
        
