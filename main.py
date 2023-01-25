def get_num_of_words(words):
    return len(words)

def get_character_occurrences(contents):
    # convert any uppercase letters to lowercase
    contents = contents.lower()

    # create dictionary
    char_occurrences = {}
    # iterate over the string
    for keys in contents:
        # add characters to the dictionary as keys with the number as the value
        # .get() => if keys is new it will assign 0 as the init value and add 1
        # otherwise it will add one to the existing value
        char_occurrences[keys] = char_occurrences.get(keys, 0) + 1
    return char_occurrences

def get_value(key):
    return key[1]

def print_report(words, char_dictionary):
    print('--- Begin report of books/frankenstein.txt ---')
    print(f'{get_num_of_words(words)} words found in the document\n')

     # convert dictionary to a list
    char_list = list(char_dictionary.items())
    # sort in descending order by the number of occurrences
    char_list.sort(reverse=True, key=get_value)

    for string_char in char_list:
        # avoid printing out special characters
        if string_char[0].isalpha():
            print(f"The '{string_char[0]}' character was found {string_char[1]} times")
    
    print('--- End report ---')

def main():
    print('reading book...\n')

    # with is block that will do a close() for you
    # when using just open(), you will have to use close() when done with a file
    with open('books/frankenstein.txt') as book:
        # reading the file contents into a string
        book_contents = book.read()

    # spliting the words into an array
    book_words = book_contents.split()

    # create dictionary with occurrences of each character
    char_occurrences_dict = get_character_occurrences(book_contents)

    # print out the report
    print_report(book_words, char_occurrences_dict)

main()