text = input("Enter a sentence: ")

words = text.split()
freq = {}

for word in words:
    word = word.lower()  
    if word in freq:
        freq[word] += 1
    else:
        freq[word] = 1

print("\nWord Frequency:")
for word, count in freq.items():
    print(word, ":", co
