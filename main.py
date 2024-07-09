with open('books/frankenstein.txt') as f:
    file_contents = f.read()

words = file_contents.split()
print("--- Begin report of books/frankenstein.txt ---")
print(f"{len(words)} words found in the document")
print("\n\n")
alphabets = list(map(chr, range(97, 123)))
for alphabet in alphabets:
    if file_contents.lower().count(alphabet) > 0:
        print(f"The {alphabet} character was found {file_contents.lower().count(alphabet)} times")