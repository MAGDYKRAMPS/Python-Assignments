sentence = input("Enter a sentence: ")
modified_sentence = ""

for char in sentence:
    if char.lower() in 'aeiou':
        continue
    
    modified_sentence += char

print("Modified sentence:", modified_sentence)
