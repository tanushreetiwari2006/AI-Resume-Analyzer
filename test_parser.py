from parser import extract_text

text = extract_text("resume.pdf")
print(text)
print("---")
print("Total characters:", len(text))