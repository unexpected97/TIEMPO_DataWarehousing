user_input = input("Please enter a sentence or words: ")
words = user_input.split()
word_count = 0
for word in words: 
    print(word) 
    word_count += 1
print("Total number of words:", word_count)
