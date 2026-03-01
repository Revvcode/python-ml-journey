# replace is a string method which takes 2 args 
# removeprefix removes the starting part of a string
# re.sub(pattern, repl,string)

import re

url = input("URL: ").strip()

if matches := re.search(r"^https?://(?:www\.)?twitter\.com/([a-z0-9_]+)$", url , re.IGNORECASE):
    print(f"username: ",matches.group(1))