#1
words = input("Enter words separated by commas: ")

words_list = words.split(",")


words_list.sort()


sorted_words = ",".join(words_list)


print(sorted_words)

#2
def longest_word(sentence):
    # Step 2: Split the sentence into words
    words = sentence.split()

 
    longest = words[0]


    for word in words:
        if len(word) > len(longest):
            longest = word


    return longest
