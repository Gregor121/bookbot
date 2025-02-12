with open("books/frankenstein.txt") as f:
    file_contents = f.read()
def word_count(string):
    count = len(string.split())
    print(count)

word_count(file_contents)
