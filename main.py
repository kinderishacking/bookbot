
import os
def main():
    # with open('books/frankenstein.txt') as f:
    #     file_contents = f.read()
    #     print(file_contents)
    #     count_words(file_contents)
    #     chars = count_characters(file_contents)
    #     #print(chars)
    
    report('books/frankenstein.txt')








def count_words(text):
    words = text.split()

    return len(words)


def sort_on(item):
    return item[0]


def report(file_path):

    with open(file_path) as f:
        file_contents = f.read()

        #print(file_contents)


        c_words = count_words(file_contents)

        chars = count_characters(file_contents)
        #print(chars)
        #list_of_dicts = [{key: value} for key, value in chars.items()]

        
        chars = dict(sorted(chars.items(), key=sort_on))
        sorted_dict_desc = dict(sorted(chars.items(), key=lambda item: item[1], reverse=True))
        #print(sorted_dict_desc)
        #print(chars)
        print(f"--- Begin report of {os.path.basename(file_path)} ---")
        print(f"{c_words} words found in the document")
        #print("\n")

        for char, value in sorted_dict_desc.items():

            #print(type(char))
            
            if char.isalpha():
                print(f"The '{char}' character was found {value} times.")

        print("--- End report ---")
                




def count_characters(text):
    char_dict = {}

    for char in text.lower():

        if char in char_dict:
            char_dict[char] += 1

        else:
            char_dict[char] = 1

    return char_dict


if __name__ == "__main__":
    main()

