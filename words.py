words = "hello", "hey", "yo", "yes"

def print_upper_words(words, must_start_with):
    a = []
    a.extend(must_start_with)
    for word in words:
        if word[0] in a:
            print(word.upper())


print_upper_words(words, must_start_with={"y"})