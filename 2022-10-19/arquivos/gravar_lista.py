listitems = ["ab", "cd", "2", "6"]

with open('abc.txt', 'w') as temp_file:
    for item in listitems:
        temp_file.write("%s " % item)
file = open('abc.txt', 'r')
print(file.read())