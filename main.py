def main():
    with open("./books/frankenstein.txt") as f:
        file_contents = f.read()
        char_results = count_chars(file_contents)
        
        print("--- Begin report of books/frankenstein.txt ---")
        print(f"{count_words(file_contents)} words found in the document\n")

        for char in char_results:
            print(f"The '{char}' character was found {char_results[char]} times")

def count_chars(words):
    result = {}
    for char in words:
        if char.isalpha():
            char = char.lower()
            if char not in result:
                result[char] = 1
            else:
                result[char] += 1
    return result

def count_words(words):
    return len(words.split())
    

main()