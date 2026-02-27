# RE (regular expression) library helps to check and replace patterns
# re.search(pattern,string) returns boolean \w word character, number and underscore \d decimal digit \D not a decimal digit \s whitespace

import re

email = input("what's your email? ").strip()

if re.search(r"^\w+@\w+\.(com|edu)$", email, re.IGNORECASE):
    print("Valid")
else:
    print("invalid")