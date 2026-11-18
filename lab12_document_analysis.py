sentence = input("Enter a sentence: ")

total_characters = len(sentence)

words = len(sentence.split())

vowels = sum(1 for ch in sentence if ch.lower() in "aeiou")

consonants = sum(1 for ch in sentence if ch.isalpha() and ch.lower() not in "aeiou")

digits = sum(1 for ch in sentence if ch.isdigit())

spaces = sum(1 for ch in sentence if ch == " ")

special = sum(1 for ch in sentence if not ch.isalnum() and ch != " ")

letters = vowels + consonants

percentage = (vowels / letters * 100) if letters > 0 else 0

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
