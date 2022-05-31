#we need to create a list of integers which specify the length of each word in a certain sentence, but only if the word is not the word "the".
sentence = "the quick brown fox jumps over the lazy dog"
words = sentence.split()
word_len = [len(word) for word in words if word != "the"]
print(words)
print(word_len)


#Exercise: create a new list called "newlist" out of the list "numbers", which contains only the positive numbers from the list, as integers.
numbers = [34.6, -203.4, 44.9, 68.3, -12.2, 44.6, 12.7]
newlist = [int(number) for number in numbers if number > 0]
print(newlist)
