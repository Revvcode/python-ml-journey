# sorted(list_name), sorts the list alphabetically
# files help with persistent storage
# open helps access a file that exists in a system, open("name_of_text", "w or r or a"), w rewrites the whole file, default is r
# .write helps insert text into a file
# with automatically opens and closes a file
# readlines helps read each line
# rstrip removes ending characters from right end

names = []

with open("names.txt") as file:
    for line in file:
        names.append(line.rstrip())

for name in sorted(names,reverse=True):
    print(f"hello, {name}")