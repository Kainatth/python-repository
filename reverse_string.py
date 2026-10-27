text = "python"
reversed_text = text[::-1]

print("Reversed:", reversed_text)

text = "python"
reversed_text = ""

for ch in text:
    reversed_text = ch + reversed_text

print("Reversed:", reversed_text)