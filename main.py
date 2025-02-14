with open("books/frankenstein.txt") as f:
    file_contents = f.read()
    

def word_count(string):
    count = len(string.split())
    print(count)

def string_count(string):
    strings = {}
    file_contents = string.lower()
    for character in file_contents:
        if character in strings.keys():
            strings[character] += 1
        else:
            strings.update({character: 1})
    print(strings)

string_count(file_contents)

