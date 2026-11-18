sentence = input("Enter a sentence: ")

# Count characters
total_characters = len(sentence)

# Count words
words = len(sentence.split())

# Count vowels
vowels = sum(1 for ch in sentence if ch.lower() in "aeiou")

# Count consonants
consonants = sum(1 for ch in sentence if ch.isalpha() and ch.lower() not in "aeiou")

# Count digits
digits = sum(1 for ch in sentence if ch.isdigit())

# Count spaces
spaces = sum(1 for ch in sentence if ch == " ")

# Count special characters
special = sum(1 for ch in sentence if not ch.isalnum() and ch != " ")

# Calculate total letters
letters = vowels + consonants

# Calculate vowel percentage
percentage = (vowels / letters * 100) if letters > 0 else 0

# Display report
print("\n" + "=" * 40)
print("DOCUMENT ANALYSIS REPORT")
print("=" * 40)

print("Sentence:", sentence)
print("Total characters:", total_characters)

print("\n--- Character Breakdown ---")
print("Words:", words)
print("Vowels:", vowels)
print("Consonants:", consonants)
print("Digits:", digits)
print("Spaces:", spaces)
print("Special characters:", special)

print("\n--- Summary ---")
print("Total letters:", letters)
print("Vowel percentage: {:.1f}%".format(percentage))

print("\n" + "=" * 40)
print("Analysis Complete!")
print("=" * 40)
