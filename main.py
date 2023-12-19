def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    report(book_path, text)



def get_num_words(text):
    words = text.split()
    return len(words)


def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_book_letters(text):
    letter_count = {} #store letter count
    symbol_count = {} #store symbol count incase needed 
    text_with_no_space = text.replace(" ", "") #remove spaces from the text

    #loop through each character in the text
    for x in text_with_no_space:
        if (x.isalpha()): #if the character is a letter
            letter = x.lower() #make all letters lowercase
            if letter in letter_count:
                letter_count[letter] += 1 #if letter is in dict already add count
            else:
                letter_count[letter] = 1 #if letter isn't in dict yet add it with starting value 1
        else:  #if the character is a symbol
            if x in symbol_count:
                symbol_count[x] += 1
            else:
                symbol_count[x] = 1

    return letter_count

def sort_dict(dictionary):
    sorted_tuple = sorted(dictionary.items(), key=lambda x:x[1], reverse=True)
    sorted_dict = dict(sorted_tuple)
    return sorted_dict

def report(title, text):

    num_words = get_num_words(text)
    letters_dict = get_book_letters(text)
    sorted_letters_dict = sort_dict(letters_dict)

    print("--- Book Report ---")
    print(f"{title}")
    print(f"{num_words} words found in document")
    
    for letter in sorted_letters_dict:
        print(f"{letter} was used {sorted_letters_dict[letter]} times")

    print("--- Report End ---")

main()
