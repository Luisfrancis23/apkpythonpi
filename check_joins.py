import re

file_path = r'C:\Users\WK\Pictures\app\main.py'

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Find lines that contain MD tags or Image tags not at the start of the line
# (ignoring leading spaces)
matches = re.findall(r'[^\n ] *(?:MD|Image|ScrollView|MDScreen)[^:\n]*:', content)

if matches:
    print("Potential joined lines found:")
    for m in matches:
        print(f"'{m}'")
else:
    print("No joined lines found.")
