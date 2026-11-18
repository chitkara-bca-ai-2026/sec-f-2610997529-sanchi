
sentence = input("Enter a sentence: ")

position = int(input("Enter position for indexing: "))

if 0 <= position < len(sentence):
    character = sentence[position]
else:
    character = "Invalid position"

start = int(input("Enter start index for slicing: "))
end = int(input("Enter end index for slicing: "))

sliced = sentence[start:end]

upper = sentence.upper()
lower = sentence.lower()

old_word = input("Enter word to replace: ")
new_word = input("Enter replacement word: ")

replaced = sentence.replace(old_word, new_word)

length = len(sentence)

print("\n================================")
print("       TEXT PROCESSING TOOL")
print("================================")

print("Character at position:", character)
print("Sliced string:", sliced)
print("Uppercase:", upper)
print("Lowercase:", lower)
print("After replace:", replaced)
print("Length of sentence:", length)

print("================================")
print("Analysis Complete!")