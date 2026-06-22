word = input("Enter word: ")

counts = {}

for char in word:
    if char in counts:
        counts[char] += 1
    else:
        counts[char] = 1

print(counts)