import re

phone = input()
pattern = r"^[+49][0-9]{7}+$"

if re.match(pattern, phone):
    print("Valid")
else:
    print("Invalid")